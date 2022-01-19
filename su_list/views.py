from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from su_list import models
from su_list.forms import SeriousNoUrgentListForm, SeriousYesUrgentListForm

def list(request: HttpRequest):
    return render(request, "su_list/sulist_detail.html")



# 중요하지만 급하지 않아 list
@login_required
def green_list_(request: HttpRequest):
    green_list = models.SeriousNoUrgentList.objects.filter(user_id=request.user.id)
    return render(request, "su_list/sulist_detail.html", {"green_list": green_list})

# 중요하고 급해 list
@login_required
def red_list_(request: HttpRequest):
    red_list = models.SeriousNoUrgentList.objects.filter(user_id=request.user.id)
    return render(request, "su_list/sulist_detail.html", {"red_list": red_list})



# 중요하지만 급하지 않아 views
@login_required
def green_list_create(request:HttpRequest):
    form = SeriousNoUrgentListForm()

    if request.method == "POST":
        form = SeriousNoUrgentListForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "성공")
            return redirect('su_list:list')

    return render(request, 'su_list/sulist_detail.html', {
        "form":form,


    })


# 중요하고 급해 views
@login_required
def red_list_create(request: HttpRequest):
    form = SeriousYesUrgentListForm()

    if request.method == "POST":
        form = SeriousYesUrgentListForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "성공")
            return redirect('su_list:list')

    return render(request, 'su_list/sulist_detail.html', {
        "form": form,

    })
