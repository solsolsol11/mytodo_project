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
def list(request: HttpRequest):
    return render(request, "su_list/sulist_detail.html")


@login_required
def list_create(request:HttpRequest):
    form = SulistForm()
    print("실행")
    if request.method == "POST":
        form = SulistForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "성공")
            return redirect('su_list:list')
        print("실행2")
    return render(request, 'su_list/sulist_detail.html', {
        "form":form

    })

