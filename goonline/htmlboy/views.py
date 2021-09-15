from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeguy(request):
    return render(request, 'homepage/homepage.html')
def first(request):
    return render(request, 'homepage/first.html')
def second(request):
    return render(request, 'homepage/second.html')
def third(request):
    return render(request, 'homepage/third.html')
def fourth(request):
    return render(request, 'homepage/fourth.html')

def test(request):
    skills = ['Backend Development', 'Html+CSS Dev', 'Cooking!', 'Not Becoming Fat After Eating Too Much']
    return render(request, 'homepage/test.html', {'skills':skills})