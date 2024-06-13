from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def getTodos(request):
  todos = Todo.objects.all()
  serializer = TodoSerializer(todos, many=True)
  return Response(serializer.data)

