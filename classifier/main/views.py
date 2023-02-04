from django.shortcuts import render, redirect
from .models import Story, TagsModel
from .forms import StoryForm, ProductFilter
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView, DeleteView

def product_list(request):
    filter = ProductFilter(request.GET, queryset=Story.objects.all())
    return render(request, 'main/index.html', {'filter': filter})


def index(request):
    tasks = Story.objects.all()
    count = tasks.count()
    choices = TagsModel.objects.all()
    answer = ''
    kateg = ''
    if request.method == 'POST':
        answer = int(request.POST.get('filter_by'))

        #tags = "в категории " + str(TagsModel.objects.get(tagId=answer).tagName)
        if answer == 1:
            tasks = Story.objects.filter(classif = 'Сказки о животных')
        else:
            tasks = Story.objects.filter(classif = 'Волшебные сказки')
        count = tasks.count()
    # forDifferent = FilterTag()
    context = {
        'title': 'Главная страница сайта',
        'tasks': tasks,
        'choices': choices,
        'count': count,
    }
    return render(request, 'main/index.html', context)



def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"

    form = StoryForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def story(request):
    tasks = Story.objects.filter(classif = 'Волшебные сказки')
    return render(request, 'main/story.html', {'tasks': tasks})

    #return render(request, 'main/story.html')

def story_2(request):

    tasks = Story.objects.filter(classif='Сказки о животных')
    return render(request, 'main/story_2.html', {'tasks': tasks})

    #return render(request, 'main/story_2.html')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ResumeForm

# Создайте здесь представления.

def upload_resume(request):
    error = ''
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/resume/')
        else:
            error = "Форма была неверной"
    else:
        form = ResumeForm()
    return render(request, 'files/resume.html', {'form':form})

from .classificator import MainClassify as MC
from .forms import NewForm, TextsFormSecond

def classify(request):
    error = ''
    classText = ''
    if request.method == 'POST':
        form = TextsFormSecond(request.POST)
        secondForm = NewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text_news")
            classText = MC.choose_class(text)
        else:
            error = 'Попробуйте ввести другие данные'
    form = NewForm()
    secondForm = NewForm()
    context = {
        'form': form,
        'error': error,
        'predict': classText
    }
    return render(request, 'main/classify.html', context)

def my_test_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)

def showAll(request):
    news = Story.objects.all()
    count = news.count()
    return index(request)
