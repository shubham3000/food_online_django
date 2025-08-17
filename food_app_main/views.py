from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = [
        {'message': 'Welcome to the Food App!'},
        {'message': 'Try our new dishes!'},
        {'message': 'Order now and get a discount!'}
    ]
    return render(request, 'home.html', {'context': context})