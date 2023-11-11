from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=True)    
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}), required=True, max_length=20, min_length=4)
    class Meta:
        model= Profile

class SignupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}), required=True, max_length=20, min_length=4)
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}), required=True, max_length=20, min_length=4)

    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=True)    
    
    name = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), required=False)    
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class":"form-control"}), required=True)    
    img = forms.ImageField(widget=forms.FileInput(attrs = {"class":"form-control"}), required=False)
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password']
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
