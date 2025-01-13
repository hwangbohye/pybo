from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): #UserCreationForm 상속 받음(username, password1, password2 속성)
    email = forms.EmailField(label="이메일") # email 속성 추가

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")