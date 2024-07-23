from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
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
            return redirect('users-login')

    else:
        print("vbbbbbbbbbbbbbbbbbbbbbbb")
        # form = UserCreationForm()
        form = SignUpForm()
    context = {
        'form' : form
    }
    print("sssssssssssss")
    return render(request, 'users/sign_up.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form' : u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)