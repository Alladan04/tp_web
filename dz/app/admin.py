from django.contrib import admin
from .models import Question, QuestionLike, TagQuestion, Tag, Answer, AnswerLike, Profile, UserLike, User

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionLike)
admin.site.register(TagQuestion)
admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(AnswerLike)
admin.site.register(Profile)
admin.site.register(UserLike)







