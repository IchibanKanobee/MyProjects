from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlatformForm, RecordTypeForm


def index(request):
    return HttpResponse("Hello, world. I am your asset manager!")

def add_platform(request):
    if request.method == "POST":
        form = PlatformForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_platform.html', {})
    else:
        return render(request, 'add_platform.html', {})


def add_record_type(request):
    if request.method == "POST":
        form = RecordTypeForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_record_type.html', {})
    else:
        return render(request, 'add_record_type.html', {})
