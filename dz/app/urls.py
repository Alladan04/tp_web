from django.contrib import admin
from django.urls import path
from app.views import index, ask, question, settings, log_in, signup, hot, tag, search, log_out
urlpatterns = [
    path('', index, name = 'basic_url'),
    path ('hot/',hot, name = 'hot_url' ),
    path ('tag/<str:tag_name>/', tag, name = 'tag_url'),
    path('question/<int:id>', question, name = 'question_url'), 
    path('login/', log_in, name = 'login_url'), 
    path('logout/', log_out,name = 'logout_url'),
    path('settings/', settings, name = 'settings_url'), 
    path('search/', search, name= "search_url"),
    path('ask/' ,ask, name = 'ask_url'),
    path('signup/' ,signup, name = 'signup_url'),
    path('admin/', admin.site.urls),
]
