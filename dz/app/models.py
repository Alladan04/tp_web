from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#from .managers import QuestionManager, AnswerManager, TagManager, TagQuestionManager, ProfileManager

class QuestionManager(models.Manager):
     def get_all(self):
          return self.all()
     
     def get_new(self):
          return self.all().order_by('-creation_date')
     
     def get_hot(self, limit:int|None):
          '''if limit:
               return self.all().order_by('-rating')[0:limit]
          else :
               return self.all().order_by('-rating')'''
          likes = (QuestionLike.objects
          .values('question')
          .annotate(qcount=models.Count('question'))
          .order_by(('-qcount')))
          if limit and limit<likes.count():
               likes = likes[0:limit]
          questions = [Question.objects.get(id=lk['question']) for lk in likes]
          return questions
        
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
     

#Пользователь – электронная почта, никнейм, пароль, аватарка, дата регистрации, рейтинг.
class Profile(models.Model):
    #nickname = models.CharField(max_length=150, unique=True)
    #email = models.CharField(max_length=150, blank=True, null=True)
    #creation_date = models.DateTimeField(blank=False,null = False) ==date_joined
    img= models.CharField(max_length=150,blank =True, null = True)
    rating = models.IntegerField(blank = True, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null=True)
    objects = ProfileManager()
    class Meta:
        managed = True
        db_table = 'profiles'
'''@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''


#Вопрос – заголовок, содержание, автор, дата создания, теги, рейтинг.
   
class Question(models.Model):
     id = models.BigAutoField(auto_created=True, primary_key=True)
     title = models.CharField(max_length=256, null = False, blank = False)
     text = models.CharField(max_length=500, null = True, blank=True)
     author = models.ForeignKey(User, models.DO_NOTHING, blank= True, null = True)
     creation_date = models.DateTimeField(blank=True, null=True)
     rating = models.IntegerField(blank = True, null = True)
     objects = QuestionManager()
     class Meta:
        managed = True
        db_table = 'questions'

#Ответ – содержание, автор, дата написания, флаг правильного ответа, рейтинг.
class Answer(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    text = models.CharField(max_length=500, null = True, blank=True)
    creation_date = models.DateTimeField(blank=True, null = True)
    is_correct = models.BooleanField(blank = True, null = True)
    rating = models.IntegerField(blank = True, null = True)
    question = models.ForeignKey('Question',models.DO_NOTHING, blank= True, null = True )
    author = models.ForeignKey(User, models.DO_NOTHING, blank= True, null = True)
    objects = AnswerManager()
    class Meta:
        managed = True
        db_table = 'answers'

#Тег – слово тега.
class Tag(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    objects = TagManager()
    class Meta:
        managed = True
        db_table = 'tags'
#вспомогательная таблица для реализации связи многие-ко-многим
class TagQuestion(models.Model):
    tag = models.ForeignKey('Tag',models.DO_NOTHING, blank= True, null = True)
    question = models.ForeignKey('Question',models.DO_NOTHING, blank= True, null = True)
    objects = TagQuestionManager()
    class Meta:
        managed = True
        db_table = 'tag_question'
#таблицы с лайками для вопросов/ответов/профилей
class QuestionLike(models.Model):
    question = models.ForeignKey('Question',models.DO_NOTHING, blank= True, null =True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank= True, null = True)
    class Meta:
        managed = True
        db_table = 'question_like'

class AnswerLike(models.Model):
    answer = models.ForeignKey('Answer',models.DO_NOTHING, blank= True, null = True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank= True, null = True)
    class Meta:
        managed = True
        db_table = 'answer_like'

class UserLike(models.Model):
    from_user= models.ForeignKey(User, models.DO_NOTHING, blank= True, null = True, related_name="like_from_user")
    to_user = models.ForeignKey(User, models.DO_NOTHING, blank= True, null = True, related_name="like_to_user")
    class Meta:
        managed = True
        db_table = 'user_like'