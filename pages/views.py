from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def team(request):
    return render(request, 'pages/team.html')

def contact(request):
    return render(request, 'pages/contact.html')