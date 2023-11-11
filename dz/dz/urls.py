"""
URL configuration for dz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
