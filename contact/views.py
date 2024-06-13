from django.shortcuts import render
from .models import contactdb

# Create your views here.
def contact(request):
    name =request.POST.get("name")
    email =request.POST.get("email")
    phone =request.POST.get("phone")
    subject =request.POST.get("subject")
    message =request.POST.get("message")
    data=contactdb(name=name,email=email,phone=phone,subject=subject,message=message)
    if request.method == 'POST':
        data.save()

    


    return render(request, 'contact/contact.html')
