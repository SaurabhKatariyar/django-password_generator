from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    isupper = request.GET.get('uppercase')
    isnum = request.GET.get('numbers')
    isspcl = request.GET.get('special')
    if isupper:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if isnum:
        characters.extend(list('0123456789'))
    if isspcl:
        characters.extend(list('!@#$%^&*()'))
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about_us(request):
    return render(request, 'generator/about_us.html')