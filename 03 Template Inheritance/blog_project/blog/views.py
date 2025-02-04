from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def conatcts(request):
    return render(request, 'blog/contacts.html')

def services(request):
    return render(request, 'blog/services.html')