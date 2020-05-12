from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistrationForm
from .models import Profile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('/')

        context = {"form": form}
        return render(request, 'users/login.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        next = request.GET.get('next')
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect('/')

        context = {"form": form}
        return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    return render(request, 'users/profile.html', context)


def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    profile.mobile = request.POST['mobile']
    profile.address = request.POST['address']
    profile.save()
    print(request.POST['address'])
    return redirect('/')
