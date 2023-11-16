from django.contrib import admin
from django.urls import path

from app.views import index, ask, question, settings, login, signup, hot, tag, search
urlpatterns = [
    path('', index, name = 'basic_url'),
    path ('hot/',hot, name = 'hot_url' ),
    path ('tag/<str:tag_name>/', tag, name = 'tag_url'),
    path('question/<int:id>', question, name = 'question_url'), 
    path('login/', login, name = 'login_url'), 
    path('settings/<int:user_id>', settings, name = 'settings_url'), 
    path('search/', search, name= "search_url"),
    path('ask/' ,ask, name = 'ask_url'),
    path('signup/' ,signup, name = 'signup_url'),
    path('admin/', admin.site.urls),
]
