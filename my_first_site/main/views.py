from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def index(request):
    data ={
        'title': 'Главная страница !!!',
        'values' : ['some','Hello','124']
    }
    return render(request, 'main/index.html',data)

def about(request):
    return render(request,'main/about.html')