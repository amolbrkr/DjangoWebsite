from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request): 
  return HttpResponse("WHatver.")

def modi(request):
  return HttpResponse("Wah modi ji wah.")
