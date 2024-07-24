from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets
from .models import Answer
from .serializers import AnswerSerializer


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'This is the message from django!'})


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer