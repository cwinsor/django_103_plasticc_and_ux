from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'starchaser/welcome.html')


def info(request):
    return render(request, 'starchaser/info.html')
