from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "test.html")

def next(request):
    return render(request, 'next.html')

