from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Vaibhav'})


def add(request):
    va11 = int(request.POST['num1'])
    va12 = int(request.POST['num2'])
    sum = va11 + va12
    return render(request, 'result.html', {'result':sum})
