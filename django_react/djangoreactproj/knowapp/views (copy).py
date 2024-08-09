from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subject, Question
from .serializers import QuestionSerializer, SubjectSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'This is the message from django!'})


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
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)



class QuestionPagination(PageNumberPagination):
    page_size = 1  # Number of questions per page
    page_size_query_param = 'page_size'
    max_page_size = 100



@api_view(['GET'])
def question_list(request):
    subject_id = request.GET.get('subject_id')

    # Get the selected subject
    subject = Subject.objects.filter(id=subject_id).first()

    if not subject:
        return Response({'detail': 'Subject not found'}, status=404)
    
    questions = Question.objects.filter(subject_id=subject_id)
    paginator = QuestionPagination()
    result_page = paginator.paginate_queryset(questions, request)
    serializer = QuestionSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

    '''
    # Get all descendant subjects, including the selected subject
    descendant_subjects = subject.get_all_descendants() | {subject}
    
    logger.debug("Descendant subjects: {}", descendant_subjects)

    # Filter questions by these subjects
    questions = Question.objects.filter(subject__in=descendant_subjects)
    
    logger.debug("Questions: {}", questions)

    # Paginate the queryset
    paginator = QuestionPagination()
    result_page = paginator.paginate_queryset(questions, request)
    
    # Serialize and return the paginated response
    serializer = QuestionSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
   '''
 