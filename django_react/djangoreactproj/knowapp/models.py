from django.db import models
from django.conf import settings
import os

def get_image_upload_path(instance, filename):
    return os.path.join(settings.IMAGE_UPLOAD_DIR, filename)

def get_video_upload_path(instance, filename):
    return os.path.join(settings.VIDEO_UPLOAD_DIR, filename)


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    answer_text = models.TextField()
    image = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True)
    video = models.FileField(upload_to=get_video_upload_path, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

