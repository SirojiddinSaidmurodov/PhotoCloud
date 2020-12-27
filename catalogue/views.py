# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from catalogue import forms
from catalogue.models import PhotoMetaData


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def account(request):
    return render(request, 'account.html')


@login_required
def upload(request):
    if request.method == 'POST':
        form = forms.UploadForm(request)
        if form.is_valid():
            meta: PhotoMetaData = form.save(commit=False)
            photo = form.cleaned_data.get('photo')
            user: User = request.user
            meta.user = user
            meta.save()
        return redirect('upload')
    else:
        form = forms.UploadForm()
    return render(request, 'catalogue/upload.html', {'form': form})
