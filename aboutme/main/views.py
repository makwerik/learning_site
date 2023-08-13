from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'main/index.html')

def text(requests):
    return render(requests, 'main/text.html')
