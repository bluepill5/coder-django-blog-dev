from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Modelos
from blogApp.models import *
# Formularios

# Views
def home(request):
    return render(request, './blogApp/home.html')

def about(request):
    return render(request, './blogApp/about.html')

def pages(request):
    pages = Blog.objects.all()
    return render(request, './blogApp/pages.html', {'pages': pages})

def formBlog(request):
    if request.method == 'POST':
        # Guardamos el blog
        blog = Blog(user=request.POST['user'], title=request.POST['title'])
        blog.save()
        # Guardamos el artículo
        article = Article(title=request.POST['title'], 
                           text_article=request.POST['text_article'], 
                           topic=request.POST['topic'], 
                           date_creation=request.POST['date_creation'])
        article.save()

        return render(request, './blogApp/home.html')
    return render(request, './blogApp/formBlog.html')

def search(request):
    return render(request, './blogApp/search.html')

def login(request):
    return render(request, './blogApp/login.html')

def signup(request):
    return render(request, './blogApp/signup.html')
