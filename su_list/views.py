from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_POST

from su_list import models
from su_list.forms import SeriousNoUrgentListForm, SeriousYesUrgentListForm, NoSeriousNoUrgentForm, \
    NoSeriousYesUrgentForm
from su_list.models import SeriousNoUrgentList, SeriousYesUrgentList, NoSeriousNoUrgent, NoSeriousYesUrgent


# 리스트 삭제
# 중요하지만 급하지 않아 삭제
@login_required
@require_POST
def green_list_delete(request: HttpRequest):
    print('성공')

    ids = map(int, request.POST.get('ids').split(','))

    if map(len == 0):
        messages.success(request, "성공")

    green_lists = SeriousNoUrgentList.objects.filter(id__in=ids)

    for green_list in green_lists:
        if green_list.user != request.user:
            raise PermissionError()
        green_list.delete()
    print('성공')
    messages.success(request, "선택삭제완료")

    return redirect('su_list:list')


# 리스트 삭제
# 중요하고 급해 삭제
@login_required
def red_list_delete(request: HttpRequest):
    print('성공')

    red_list = models.SeriousYesUrgentList.objects.filter(user_id=request.user.id)

    red_list.delete()
    print('성공')
    messages.success(request, "삭제완료")

    return redirect('su_list:list')

# 리스트 삭제
# 중요하지도 않고 급하지도 않아 삭제
@login_required
def gray_list_delete(request: HttpRequest):
    print('성공')

    gray_list = models.NoSeriousNoUrgent.objects.filter(user_id=request.user.id)

    gray_list.delete()
    print('성공')
    messages.success(request, "삭제완료")

    return redirect('su_list:list')

# 리스트 삭제
# 중요하진 않은데 급해 삭제
@login_required
def gold_list_delete(request: HttpRequest):
    print('성공')

    gold_list = models.NoSeriousYesUrgent.objects.filter(user_id=request.user.id)

    gold_list.delete()
    print('성공')
    messages.success(request, "삭제완료")

    return redirect('su_list:list')


# ALL LIST
@login_required
def all_list(request: HttpRequest):
    green_list = models.SeriousNoUrgentList.objects.filter(user_id=request.user.id)
    red_list = models.SeriousYesUrgentList.objects.filter(user_id=request.user.id)
    gray_list = models.NoSeriousNoUrgent.objects.filter(user_id=request.user.id)
    gold_list = models.NoSeriousYesUrgent.objects.filter(user_id=request.user.id)
    return render(request, "su_list/sulist_detail.html", {
        "green_list": green_list,
        "red_list": red_list,
        "gray_list": gray_list,
        "gold_list": gold_list,

    })


# 테스트 케이스
def test_case(request: HttpRequest):
    return render(request, "su_list/test_case.html")


# 중요하지만 급하지 않아 views
@login_required
def green_list_create(request: HttpRequest):
    form = SeriousNoUrgentListForm()
    print(form)
    if request.method == "POST":
        form = SeriousNoUrgentListForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "성공")
            print("성공")
            return redirect('su_list:list')

    return render(request, 'su_list/sulist_detail.html', {
        "form": form,

    })


# 중요하고 급해 views
@login_required
def red_list_create(request: HttpRequest):
    form = SeriousYesUrgentListForm()
    print(form)
    if request.method == "POST":
        form = SeriousYesUrgentListForm(request.POST)
        if form.is_valid():
            article2 = form.save(commit=False)
            article2.user = request.user
            article2.save()
            messages.success(request, "성공")
            print("성공")
            return redirect('su_list:list')

    return render(request, 'su_list/sulist_detail.html', {
        "form": form,

    })


# 중요하지도 않고 급하지도 않아 views
@login_required
def gray_list_create(request: HttpRequest):
    form = NoSeriousNoUrgentForm()
    print(form)
    if request.method == "POST":
        form = NoSeriousNoUrgentForm(request.POST)
        if form.is_valid():
            article3 = form.save(commit=False)
            article3.user = request.user
            article3.save()
            messages.success(request, "성공")
            print("성공")
            return redirect('su_list:list')

    return render(request, 'su_list/sulist_detail.html', {
        "form": form,

    })


# 중요하진 않은데 급해 views
@login_required
def gold_list_create(request: HttpRequest):
    form = NoSeriousYesUrgentForm()
    print(form)
    if request.method == "POST":
        form = NoSeriousYesUrgentForm(request.POST)
        if form.is_valid():
            article4 = form.save(commit=False)
            article4.user = request.user
            article4.save()
            messages.success(request, "성공")
            print("성공")
            return redirect('su_list:list')

    return render(request, 'su_list/sulist_detail.html', {
        "form": form,

    })
