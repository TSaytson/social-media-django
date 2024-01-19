from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('Hello world')

def post_id(request, post_id):
  return HttpResponse(f'This is the page of post {post_id}')

def posts_list(request):
  name = 'Mariana Silva de Carvalho'
  return render(request, 'posts_list.html', {'name': name})