
from django.shortcuts import render
from .models import Post
from .models import kid
from .models import men
from .models import women
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def women_view(request):
    woment= women.objects.all()
    return render(request, 'home/women.html',{'posts': woment} )

def men_view(request):
    posts = men.objects.all()
    # ment = men.objects.all()
    return render(request, 'home/men.html',{'posts': posts}) 



def kids(request):
    kids = kid.objects.all()
    return render(request, 'home/kids.html',{'posts': kids})

def product(request, men_id):
    menp = get_object_or_404(men, pk=men_id)
    return render(request, 'home/product.html',{'men': menp})



def kidproduct(request, kid_id):
    kidprods = get_object_or_404(kid, pk=kid_id)
    return render(request, 'home/kidproduct.html',{'kidprods': kidprods})


def womenproduct(request, women_id):
    womenprods = get_object_or_404(women, pk=women_id)
    return render(request, 'home/womenproduct.html',{'womenprods': womenprods})
