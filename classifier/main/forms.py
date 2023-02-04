from .models import Story, TagsModel
from django.forms import ModelForm, TextInput, Textarea



class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title','author', 'classif', 'story']
        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
            'classif': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            }),
            'story': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание'
            }),
        }

from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['file']

import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Story
        fields = ['classif']

from .models import New


class NewForm(ModelForm):
    class Meta:  # доп. настройки
        model = New
        fields = ["title_news", "tag_news", "text_news"]
        widgets = {
            "tag_news": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введитие тег',
                'size': '95'
            }),
            "title_news": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введитие заголовок',
                'size': '95'
            }),
            "text_news": Textarea(attrs={
                'size': '95',
                'class': 'form_control',
                'placeholder': 'Введитие текст',
                'rows': '15',
                'cols': '98',
            }),
        }

class TextsFormSecond(ModelForm):
    class Meta:
        model = New
        fields = ["text_news"]
        widgets = {
            "text_news": Textarea(attrs={
                'size': '95',
                'class': 'form_control',
                'placeholder': 'Введитие текст',
                'rows': '15',
                'cols': '98',

            })
        }

class FilterTag(ModelForm):
    class Meta:
        model = TagsModel
        fields = ['tagId', 'tagName']