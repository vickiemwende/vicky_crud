from django.shortcuts import render,redirect
from .models import Recipe

def displaydata (request):
    return render(request, 'index.html')