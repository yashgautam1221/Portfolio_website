from django.shortcuts import render
from .models import Contact


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        details = Contact(name=name, email=email, subject=subject, message=message)
        details.save()

        return render(request, 'about/index.html')
    else:
        return render(request, 'about/index.html')


def port(request):
    return render(request, 'about/porfolio.html')

