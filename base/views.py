from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render







def index(request):
    return render(request, "home/main.html")



def index3(request):
    return render(request, "home/main3.html")