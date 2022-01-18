from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from su_list.forms import SulistForm
from su_list.models import Sulist

@login_required
def list(request:HttpRequest):
    su_list = Sulist.objects.filter(user=request.user)

    return render(request, "su_list/sulist_detail.html",{
        "su_list": su_list
    })

