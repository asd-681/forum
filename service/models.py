from sre_constants import CALL
from tkinter import CASCADE
from tokenize import blank_re
from turtle import title
from urllib import request
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', null=True, blank = True)
    image = models.ImageField(verbose_name = 'Картинка', null=True, blank = "True")
    created_at = models.DateTimeField(verbose_name = 'Дата создания', auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = 'Дата изменения', auto_now = True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("index")

class Comment(models.Model):
    description = models.TextField(verbose_name='Описание', null=True, blank = True)
    post = models.ForeignKey(Post, related_name = 'comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name = 'Дата создания', auto_now_add = True)
   
    def __str__(self):
        return f'{self.description}'
    
    def get_absolute_url(self):
        return reverse("index")


class Support(models.Model):

    APPLICATION_STATUS_CHOICES = [
    ('ОК', 'Обрабатывается'),
    ('ПР', 'Принято'),
    ('ОТ', 'Отказ'),
    ]

    TYPE_QUESTION_CHOICES = [
        ("RN","Возврат"),
        ("WC","Гарантийный случай"),
        ("EX","Обмен"),
        ("RP","Ремонт"),
    ]
    header = models.CharField(verbose_name='Заголовок', max_length=100)
    question = models.TextField(verbose_name='Описание вопроса', null=True, blank = True)
    type_question = models.CharField(max_length=2, choices=TYPE_QUESTION_CHOICES, default='ОК')
    date_create = models.DateField()
    application_status = models.CharField(max_length=2, choices= APPLICATION_STATUS_CHOICES, default='RN')
    date_change_status = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)