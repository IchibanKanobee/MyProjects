from django import forms
from .models import Platform, RecordType

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']

class RecordTypeForm(forms.ModelForm):
    class Meta:
        model = RecordType
        fields = ['type']