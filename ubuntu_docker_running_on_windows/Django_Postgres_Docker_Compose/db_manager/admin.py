from django.contrib import admin
from .models import Record, Platform, RecordType

# Register your models here.
admin.site.register(Record)
admin.site.register(Platform)
admin.site.register(RecordType)