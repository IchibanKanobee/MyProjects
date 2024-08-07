from django.urls import path
from .views import hello_world, add_question, add_subject, subject_list, question_list

urlpatterns = [
    path('hello-world/', hello_world, name='hello_world'),
    path('add-question/', add_question, name='add_question'),
    path('add-subject/', add_subject, name='add_subject'),
    path('subjects/', subject_list, name='subject_list'),
    path('questions/', question_list, name='question-list'),
]
