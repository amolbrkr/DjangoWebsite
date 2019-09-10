from django.shortcuts import render
from django.http import HttpResponse

from .models import ArticlePost

# Create your views here.
def index(request):
  articles = ArticlePost.objects.all()[:15]

  return render(request, 'Article/index.html', {"articles": articles})

def user(request):
  return render(request, 'Article/user.html')