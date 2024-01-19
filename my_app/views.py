from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post

# Create your views here.

def home(request):
  return HttpResponse('Hello world')

def post_id(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'post_id.html', {'post':post})

def posts_list(request):
  if 'category_id' in request.GET:
    posts = Post.objects.filter(categories=request.GET['category_id'])
  else:
    posts = Post.objects.all()
  categories = Category.objects.all()
  return render(request, 'posts_list.html', 
                {'posts': posts, 'categories': categories})