from django.http import HttpRequest, HttpResponse
from django.shortcuts import render







def index(request:HttpRequest):
    return HttpResponse("안녕")