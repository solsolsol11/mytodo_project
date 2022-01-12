from django.http import HttpRequest, HttpResponse
from django.shortcuts import render







def index(request):
    return render(request, "home/main.html")

def index2(request):
    return render(request, "home/main2.html")