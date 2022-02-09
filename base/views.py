from PIL import Image
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render







def index(request):

    return render(request, "home/main.html")

