from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'starchaser/welcome.html')


def info(request):
    return render(request, 'starchaser/info.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('player_home')
    else:
        form = UserCreationForm()
    return render(request, 'starchaser/signup.html', {'form': form})


def ref01_why_game(request):
    return render(request, 'starchaser/ref01_why_game.html')

def ref04_variety_of_approaches(request):
    return render(request, 'starchaser/ref04_variety_of_approaches.html')

def ref05_this_web_application(request):
    return render(request, 'starchaser/ref05_this_web_application.html')

def ref06_building_a_model(request):
    return render(request, 'starchaser/ref06_building_a_model.html')

def ref08_plasticc_and_kaggle(request):
    return render(request, 'starchaser/ref08_plasticc_and_kaggle.html')

def ref09_metrics(request):
    return render(request, 'starchaser/ref09_metrics.html')
