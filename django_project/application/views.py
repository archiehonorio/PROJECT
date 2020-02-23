from django.shortcuts import render
# Create your views here.

def login(request):
    return render(request, 'pages/login.html')
def register(request):
    return render(request, 'pages/register.html')
def privacy(request):
    return render(request, 'pages/privacy.html')
def index(request):
    return render(request, 'pages/index.html')
def about(request):
    return render(request, 'pages/about.html')
def region(request):
    return render(request, 'pages/region.html')
def population(request):
    return render(request, 'pages/population.html')
def age_table(request):
    return render(request, 'pages/age_table.html')
def information(request):
    return render(request, 'pages/information.html')