from django.shortcuts import render
# Create your views here.

def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def privacy(request):
    return render(request,'privacy.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def region(request):
    return render(request,'region.html')
def population(request):
    return render(request,'population.html')
def age_table(request):
    return render(request, 'age_table.html')
def information(request):
    return render(request, 'information.html')