from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Question, Answer, Subject
from .serializers import QuestionSerializer, AnswerSerializer, SubjectSerializer

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'This is the message from django!'})


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    
@api_view(['POST'])
def add_question(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def add_subject(request):
    serializer = SubjectSerializer(data=request.data)
    logger.debug("add_subject:1")
    if serializer.is_valid():
        logger.debug("add_subject:2")
        serializer.save()
        logger.debug("add_subject:3")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.debug("add_subject:4")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)