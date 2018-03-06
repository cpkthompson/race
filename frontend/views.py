from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')


def donate(request):
    return render(request, 'frontend/donate.html')


def work(request):
    return render(request, 'frontend/work.html')


def team(request):
    return render(request, 'frontend/team.html')


def bello(request):
    return render(request, 'frontend/index.html')


def news(request):
    return None
