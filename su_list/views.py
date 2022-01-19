from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from su_list import models
from su_list.forms import SulistForm
from su_list.models import Sulist

@login_required
@require_POST

@login_required
def list(request:HttpRequest):
    su_list = Sulist.objects.filter(user=request.user)
    context = {'su_list': su_list}
    print(context)
    return render(request, "su_list/sulist_detail.html",context)