from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlatformForm, RecordTypeForm, RecordForm
from .models import Platform, RecordType


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


def add_record(request):
    platforms = Platform.objects.all()
    types = RecordType.objects.all()
    if request.method == "POST":
        file_name = request.POST.get('hiddenName')
        print(file_name)
        form = RecordForm(request.POST, request.FILES)
        model_instance = form.save(commit=False)
        model_instance.file_name = file_name
        if form.is_valid():
            print('1')
            strings_input = form.cleaned_data['tags']
            print('2')
            #separated_strings = [s.strip() for s in strings_input.split(',')]  # Split by comma
            #print(separated_strings)
            
            #Save the separated strings to the database
            #model_instance.tags = separated_strings
            model_instance.save()
            
            print(3)
            form.save()
            print(4)
        return render(request, 'add_record.html', {'platforms':platforms, 'types':types})
    else:
        return render(request, 'add_record.html', {'platforms':platforms, 'types':types})
