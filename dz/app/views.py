from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Question, Tag, TagQuestion, Answer, Profile, User, QuestionLike
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm, SettingsForm, AnswerForm, AskForm,SettingsModelForm
import requests as python_requests
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
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
     auth = request.user.is_authenticated   
     raw_questions = Question.objects.get_new()
     if auth:
          user = User.objects.get(id = request.user.id)
          profile = Profile.objects.get(user = user)
     else :
          profile = None
     #qs = [{ "tags":TagQuestion.objects.get_tag_list_by_question(rq)} for rq in raw_questions]
     questions = paginate(raw_questions, request, 30)
     return render(request=request, template_name="index.html",context = {
          'questions':questions.object_list, 'page':questions, 'tag_list':get_all_tags(), 
          "auth":auth,"user" : profile, 'user_list':get_best_members()}, status=200)

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
     questions = paginate(raw_questions, request, 30)
     return render(request=request, template_name="index.html",context = {'questions':questions.object_list, 'page':questions,'tag_list':get_all_tags(),'user_list':get_best_members()}, status=200)
@csrf_protect
def question(request, id):
     try:
         question = Question.objects.get_by_id(id)
     except:
         return HttpResponse(status = 404)
     answers = Answer.objects.get_by_question(question)
     page_items = paginate(answers,request, 20)
     tags= TagQuestion.objects.get_tag_list_by_question(question)[0:3]
     auth = request.user.is_authenticated
     user= None
     if request.method =='POST' :
          form = AnswerForm(request.POST)
          if auth:
               user = Profile.objects.filter(user = User.objects.get(id = request.user.id))[0]
               if form.is_valid():
                    answer = Answer.objects.create(text = form.cleaned_data["answer"], creation_date = datetime.now(), author = user.user, question = question)
                    answer.save()
               return redirect(reverse('question_url',args=[id]))
          else:
               return redirect(reverse('login_url'))
     else:
          form=AnswerForm()

     return render(request = request,
                    template_name="question.html", context={'question':question, 
                                                            'page':page_items,
                                                              'answers':page_items.object_list, 
                                                              'tags':tags,
                                                              'tag_list':get_all_tags(),
                                                              'user_list':get_best_members(),
                                                              'form':form,
                                                              'auth':auth,
                                                              'user':user},status=200)
@csrf_protect
def ask(request):
     auth = request.user.is_authenticated
     user = None
     if request.method=='POST':
         if auth:
               form = AskForm(request.POST, request.FILES)
               if form.is_valid():
                   question= form.save(request.user)
                    
               return redirect(reverse('question_url', args=[question.id]))
         else:
              return redirect('{}?continue={}'.format(reverse('login_url'), reverse('ask_url')))
     elif request.method=='GET':
          form = AskForm()
          return render(request=request, template_name="ask.html", context = { 'tag_list':get_all_tags(),
                                                        'user_list':get_best_members(),
                                                        'auth':auth, 'form':form}, status=200)
               
          ''' form = AskForm(request.POST, request.FILES)
          if auth:
               user = Profile.objects.filter(user = request.user.id)[0]
               if form.is_valid():
                    cd = form.cleaned_data
                    question = Question.objects.create(img = cd['img'], title = cd['title'], text = cd['text'], creation_date = datetime.now(), author = user.user)
                    question.save()
                    for tag in cd['tags']:
                         if tag == '':
                              continue
                         if Tag.objects.filter (name = tag).exists():
                              f_tag= Tag.objects.filter (name = tag)[0]
                         else:
                              f_tag = Tag.objects.create(name = tag)
                              f_tag.save()
                         tq = TagQuestion.objects.create(tag =f_tag, question = question )
                         tq.save()
                    return redirect(reverse('question_url', args=[question.id]))

          else:
               return redirect('{}?continue={}'.format(reverse('login_url'), reverse('ask_url')))
     else:
          form = AskForm()
     return render(request=request, template_name="ask.html", context = { 'tag_list':get_all_tags(),
                                                        'user_list':get_best_members(),
                                                        'auth':auth, 'form':form}, status=200)'''
@csrf_protect
@login_required(login_url = 'login_url', redirect_field_name='continue')
def settings(request):
    if request.method =='GET':
         form = SettingsModelForm(initial=model_to_dict(request.user))
        
    elif request.method == 'POST':
         form = SettingsModelForm(request.POST,request.FILES, instance=request.user)
         if form.is_valid():
              form.save()
    return render (request=request, template_name="settings.html", context = {'tag_list':get_all_tags(),
                                                              'user_list':get_best_members(),'auth':auth, 'form':form}, status = 200)

@csrf_protect
def log_in(request):
     if request.method == 'POST':
        print (request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                    login(request,user)
                    return  redirect (request.GET.get('continue', 'basic_url'))#HttpResponseRedirect('{}?{}'.format(reverse(index), 'authed=True'))
            else:
                 form.add_error(None, "Неправильный логин или пароль")
     else:
        form = LoginForm()
     return render(request, 'login.html', {'form': form,'tag_list':get_all_tags(),
                                                              'user_list':get_best_members() })
    #return render(request=request, template_name="login.html", status = 200)'
@csrf_protect
def log_out(request):
     auth.logout(request)
     return HttpResponseRedirect(reverse('login_url'))
@csrf_protect
def signup(request):
    if request.method == 'POST':
          form = SignupForm(request.POST)
          print (request.POST)
          print (form.fields)
          if form.is_valid():
               cd= form.cleaned_data
               print(cd)
               user = User.objects.create(username = cd['username'],  first_name = cd['name'], email=cd['email'])
               user.set_password(cd['password'])
               profile = Profile.objects.create(user = user, img = cd['img'])
               user.save()
               profile.save()
               user = authenticate(username=cd['username'], password=cd['password'])
               return HttpResponseRedirect('{}?{}'.format(reverse(index), 'authed=True'))
    else: 
        form = SignupForm()
    return render(request, 'sign_up1.html', {'form': form, 'tag_list':get_all_tags(),
                                                              'user_list':get_best_members()})
@login_required
@csrf_protect
def like(request):
     id = request.POST.get('id')
     question = Question.objects.get(id = int(id))
     count = QuestionLike.objects.toggle_like(user = request.user, question = question)
     return JsonResponse({"count":count} )