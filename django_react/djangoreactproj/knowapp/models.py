from django.db import models

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return self.text

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

