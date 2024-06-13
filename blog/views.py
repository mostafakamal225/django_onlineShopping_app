
from django.shortcuts import render
from .models import blogdb

# Create your views here.
def blog(request):
    posts = blogdb.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})
