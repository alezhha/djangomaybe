from django.shortcuts import render

# Create your views here.
def homeguy(request):
    return render(request, 'homepage/homepage.html')