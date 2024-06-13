from django.shortcuts import render
from .models import orderrev

# Create your views here.
def orderrevv(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    # print(email)
    # print(password)
    data=orderrev(name =email,number =password)
    if request.method == 'POST':
        data.save()

    
    return render(request, 'payment/orderrev.html')
