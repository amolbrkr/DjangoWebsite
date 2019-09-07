from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request): 
  return render(request, 'Article/index.html')

def user(request):
  return render(request, 'Article/user.html')