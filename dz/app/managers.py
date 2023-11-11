from django.db import models
from datetime import datetime, timedelta, time

class QuestionManager(models.Manager):
     def get_all(self):
          return self.all()
     
     def get_new(self):
          return self.all().order_by('-creation_date')
     
     def get_hot(self, limit:int|None):
          if limit:
               return self.all().order_by('-rating')[0:limit]
          else :
               return self.all().order_by('-rating')
     ''' likes = (QuestionLike.objects
          .values('question')
          .annotate(qcount=models.Count('question'))
          .order_by(('-qcount')))
          if limit and limit<likes.count():
               likes = likes[0:limit]
          questions = (lk.question for lk in likes)
          return questions'''
        
     def find(self, input_text:str):
          return self.filter(title__icontains=input_text)
     def get_by_id(self, id:int):
          return self.get(id = id)
     
#tqs = TagQuestion.objects.get_by_question (question)
#     tags =[ {'name':tg.tag.name} for tg in tqs]

class TagManager(models.Manager):
     def get_tag_by_name(self,name):
          return self.get(name = name)
     
     def get_all(self, name):
          return self.all()
     
     
class TagQuestionManager(models.Manager):
     def get_by_tag(self, tag):
          return self.filter(tag = tag)
     
     def get_by_question(self, question):
          return self.filter(question = question)
     
     def get_questions_by_tag(self, tag):
          tqs = self.filter(tag = tag)
          questions = [tq.question for tq in tqs]
          return questions
     
     def get_tag_list_by_question(self, question):
          tqs = self.filter(question = question)
          tags = [ {'name':tg.tag.name} for tg in tqs]
          return tags


class AnswerManager(models.Manager):
     def get_by_question(self, question):
          return self.filter(question = question).order_by('-rating')

class ProfileManager(models.Manager):
     def get_top(self, n=10):
          all = self.all().order_by('-rating')
          return (all[0:min(n, len(all))])
     
