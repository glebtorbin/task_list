from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from task.models import Task

from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
    """функция выводит весь список заданий"""
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({'tasks': serializer.data})

@api_view(['GET'])
def one_task(request, id):
    '''функция выводит задание по id'''
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, many=False)
        return Response({'task': serializer.data}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'message': 'Задания с таким id не существует'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_task(request):
    '''функция создает новое задание'''
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'task': request.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Validation error'}, status=status.HTTP_400_BAD_REQUEST)