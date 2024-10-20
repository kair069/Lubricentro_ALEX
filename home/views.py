from django.shortcuts import render

# Create your views here.
# home/views.py
from django.shortcuts import render

def portada(request):
    return render(request, 'home/index1.html')
