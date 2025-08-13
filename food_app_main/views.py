from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'message': 'Welcome to the Food App!'
    }
    return render(request, 'home.html', context)