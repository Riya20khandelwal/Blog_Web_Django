from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm
# from django.http import HttpResponse

# Create your views here.

# def index(request ):
#     return HttpResponse("<h1>dgfhj</h1>")

def index(request):
    posts = PostModel.objects.all()
    if request.method == "POST":
        form  = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form' : form,
    }

    return render(request, 'blog/index.html', context)