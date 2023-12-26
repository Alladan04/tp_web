from django import forms
from .models import User, Profile, Answer 
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control ", "placeholder":"Введите логин"}), required=True)    
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control is-invalid", "placeholder":"Введите пароль"}), required=True, max_length=20, min_length=4)
    class Meta:
        model= Profile

class SignupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}), required=True, max_length=20, min_length=4)
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}), required=True, max_length=20, min_length=4)

    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=True)    
    
    name = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=False)    
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class":"form-control"}), required=True)    
    img = forms.ImageField(widget=forms.FileInput(attrs = {"class":"form-control"}), required=False)
    def clean_username(self):
        cd = self.cleaned_data
        username = cd.get('username')
        if username and User.objects.filter(username = username).exists():
            raise forms.ValidationError("Такой пользователь уже существует")
        return cd['username']
    def clean(self):
        cd = self.cleaned_data
        if cd.get('password')!=cd.get('repeat_password'):

        #if cd['password'] != cd['repeat_password']:
             self.add_error('repeat_password', "Password does not match")
        return cd
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        '''if username and User.objects.filter(username = username).exists():
            raise forms.ValidationError('Такой username уже используется в системе')'''

        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email

    class Meta:
        model = Profile
class SettingsForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=False)    
    first_name = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=False)    
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class":"form-control"}), required=False)    
    img = forms.ImageField(widget=forms.FileInput(attrs = {"class":"form-control"}), required=False)
    def clean_username(self):
        cd = self.cleaned_data
        username = cd.get('username')
        initial = self.initial['username']
        username = cd.get('username')
        if username and username!=initial and User.objects.filter(username = username).exists() :
            raise forms.ValidationError("Такой пользователь уже существует")
        return cd['username']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        initial = self.initial['email']
        username = self.cleaned_data.get('username')
        '''if username and User.objects.filter(username = username).exists():
            raise forms.ValidationError('Такой username уже используется в системе')'''

        if email and email!= initial and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email
    class Meta:
        model= User

class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"placeholder":"Type your anwer here"}))
    class Meta:
        model = Answer

class TagForm(forms.Form):
    name = forms.CharField( required=True, max_length=30)
class AskForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs = {"class":"form-control", "placeholder":"Why do people lie?"}), required=True, max_length=256, min_length=4)
    text =  forms.CharField(max_length=500, widget=forms.TextInput(attrs={"placeholder":"Type your question here"}))
    tags = forms.CharField(max_length=500, widget=forms.TextInput(attrs={"placeholder":"tag1, tag2, tag3"}), required=False)
    def clean_tags(self):
        cd = self.cleaned_data.get('tags')
        cd = cd.split(',')
        if len(cd) == 0:
            return []
        if len(cd)>3:
            raise forms.ValidationError('Максимум три тега')
        return cd
        