from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or password is incorrect!")

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, "user was successfuly looged out.")
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)

    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "topskills": topskills,
        "otherskills": otherskills
    }
    return render(request, 'users/user-profile.html', context)
