from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Question, Tag, TagQuestion, Answer, Profile, User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
import requests as python_requests
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

##########################################################################
def paginate(objects,request,   per_page = 10):
     page = request.GET.get('page', 1)
     paginator = Paginator(objects, per_page=per_page)
     try:
           return paginator.page(page)
     except:
          return paginator.page(1)   
def get_all_tags():
     #tqs = TagQuestion.objects.all()[:10]
     tqs = Tag.objects.get_top(20)
     tags = [{'name':tg.name} for tg in tqs ]
     return tags
def get_best_members():
     users_raw = Profile.objects.get_top(10)
     users = [{'name':ur.user.username} for ur in users_raw]
     return users
############################################################################
def index(request):
     if "authed" in request.GET:
         auth = request.GET.get("authed")
     else: auth = False     
     raw_questions = Question.objects.get_new()
     questions = paginate(raw_questions, request, 30)
     return render(request=request, template_name="index.html",context = {'questions':questions.object_list, 'page':questions, 'tag_list':get_all_tags(), "auth":auth,'user_list':get_best_members()}, status=200)

def hot(request):
     raw_questions = Question.objects.get_hot(None)
     questions = paginate(raw_questions, request, 30)
     return render(request=request, template_name="index.html",context = {'questions':questions.object_list, 'page':questions, 'tag_list':get_all_tags(), 'user_list':get_best_members()}, status=200)

def tag(request, tag_name):
     try:
          tag = Tag.objects.get_tag_by_name(tag_name)
     except:
           return HttpResponse( status = 404)
     raw_questions = TagQuestion.objects.get_questions_by_tag(tag)
     questions = paginate(raw_questions, request, 30)
     return render(request=request, template_name="index.html",context = {'questions':questions.object_list, 'tag_name':tag_name,'page':questions,'tag_list':get_all_tags(),'user_list':get_best_members()}, status=200)

def search(request):
     raw_questions = Question.objects.find(request.GET.get('search', ''))
     questions = paginate(raw_questions, request, 3)
     return render(request=request, template_name="index.html",context = {'questions':questions.object_list, 'page':questions,'tag_list':get_all_tags(),'user_list':get_best_members()}, status=200)

def question(request, id):
     try:
         question = Question.objects.get_by_id(id)
     except:
         return HttpResponse(status = 404)
     answers = Answer.objects.get_by_question(question)
     page_items = paginate(answers,request, 20)
     tags= TagQuestion.objects.get_tag_list_by_question(question)[0:3]
     return render(request = request,
                    template_name="question.html", context={'question':question, 
                                                            'page':page_items,
                                                              'answers':page_items.object_list, 
                                                              'tags':tags,
                                                              'tag_list':get_all_tags(),
                                                              'user_list':get_best_members()},status=200)
def ask(request):
     return render(request=request, template_name="ask.html", context = { 'tag_list':get_all_tags(),
                                                              'user_list':get_best_members(),'auth':True}, status=200)
def settings(request, user_id):
     try:
          user = Profile.objects.get(id = user_id).user
     except:
         return  HttpResponse("no such user",status = 401)
     
     return  render (request=request, template_name="settings.html", status = 200)

def login(request):
     if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                   
                    return HttpResponseRedirect('{}?{}'.format(reverse(index), 'authed=True'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
        else:
             return HttpResponse('Bad request', status = 400)
     else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form,'tag_list':get_all_tags(),
                                                              'user_list':get_best_members() })
    #return render(request=request, template_name="login.html", status = 200)


def signup(request):
    return render(request, 'signup.html', { 'tag_list':get_all_tags(),
                                                              'user_list':get_best_members()})