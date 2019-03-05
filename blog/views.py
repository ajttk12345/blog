from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs' : blogs})

def detail(request, post_id):
    detail = Blog.objects.get(id=post_id)
    return render(request, 'blog/detail.html', {'detail' : detail})