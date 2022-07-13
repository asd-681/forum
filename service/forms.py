from dataclasses import fields
from django import forms
from django.forms import ModelForm, TextInput, Select, DateInput, Textarea
from .models import Post, Comment, Support
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title" :forms.TextInput (attrs={' class':'form-control'}), 
            "description" :forms.Textarea (attrs={' class':'form-control'}),

            }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = { 
            "description" :forms.Textarea (attrs={' class':'form-control'}),

            }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = ['header','question','type_question','date_create']

        widgets = {
            "header": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
               "question": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваш вопрос'
            }),
              "type_question": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип вопроса',
                'id':"select"
            }),
             "date_create": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания заявки',
            }),
        }