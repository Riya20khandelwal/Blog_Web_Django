from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        print("wwwwwwwwwwwwww")
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        print("xxxxxxxxxxxxxxxx")
        if form.is_valid():
            print("vvvvvvvvvvvvv")
            form.save()
            print(1111111111111)
            return redirect('blog-index')

    else:
        print("vbbbbbbbbbbbbbbbbbbbbbbb")
        # form = UserCreationForm()
        form = SignUpForm()
    context = {
        'form' : form
    }
    print("sssssssssssss")
    return render(request, 'users/sign_up.html', context)
