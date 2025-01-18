from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.djt.html')

def about(request):
    return render(request, 'pages/about.djt.html')