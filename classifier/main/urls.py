from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('story', views.story, name='story'),
    path('story_2', views.story_2, name='story_2'),
    path('resume', views.upload_resume, name = 'resume' ),
    path('classify', views.classify, name='classify'),
    path('showAll', views.showAll, name='showAll'),
]
