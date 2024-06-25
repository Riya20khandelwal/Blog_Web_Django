from django.shortcuts import render
from .models import PostModel
# from django.http import HttpResponse

# Create your views here.

# def index(request ):
#     return HttpResponse("<h1>dgfhj</h1>")

def index(request):
    posts = PostModel.objects.all()

    return render(request, 'blog/index.html', 
    {'posts': posts})