from django.shortcuts import render


# Create your views here.

def about(requests):
    return render(requests, 'about/about.html')