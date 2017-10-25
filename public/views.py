from django.shortcuts import render

def index(request):
    return render(request, 'home.html', {})

def contact_us(request):
    return render(request, 'contact-us.html', {})
