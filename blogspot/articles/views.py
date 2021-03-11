from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
    articles = Articles.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {"articles": articles})


def article_detail(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form':form })