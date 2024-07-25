from django.urls import path
from .views import hello_world, add_question

urlpatterns = [
    path('hello-world/', hello_world, name='hello_world'),
    path('add-question/', add_question, name='add_question'),
]
