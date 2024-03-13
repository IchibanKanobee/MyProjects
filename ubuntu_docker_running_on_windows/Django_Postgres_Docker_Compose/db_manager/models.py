from django.db import models

class Post(models.Model):
    account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
    )
    record = models.ForeignKey(
        "Record",
        on_delete=models.CASCADE,
    )
    annotation = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, blank=True) 


class RecordType(models.Model):
    type = models.CharField()


class Record(models.Model):
    tags = models.TextField()
    filename = models.CharField()
    creation_date = models.DateTimeField(auto_now_add=True, blank=True) 
    type = models.ForeignKey(
        "RecordType",
        on_delete=models.CASCADE,
    )


class Platform(models.Model):
    name = models.CharField()


class Account(models.Model):
    platform = models.ForeignKey(
        "Platform",
        on_delete=models.CASCADE,
    )
    name = models.CharField()
    suffix = models.CharField()
    creation_date = models.DateField(auto_now_add=True, blank=True) 
