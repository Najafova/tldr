from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .forms import UserRegisterForm
from .models import *


def index(request):
    context = {}
    context["posts"] = Posts.objects.all()
    return render(request, "index.html", context)


def about(request):
    context = {}
    context["about"] = About.objects.all()
    return render(request, "about.html", context)


def post_by_tag(request, pk):
    context = {}
    context['posts'] = Posts.objects.get(pk=pk)
    return render(request, "all_post_by_tag.html", context)


def error_page(request):
    context = {}
    return render(request, '404.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def add_tldr(request):
    context = {}
    return render(request, 'add_tldr.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {'form': form})



