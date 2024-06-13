from django.shortcuts import render
from .models import aboutdb

# Create your views here.
def about(request):
    posts = aboutdb.objects.all()
    return render(request, 'about/about.html',{'posts': posts})

