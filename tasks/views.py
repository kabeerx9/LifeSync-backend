
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def list_tasks(request):
  user = request.user
  tasks = Task.objects.filter(user=user)
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
  serializer = TaskSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user=request.user)
    return Response(serializer.data, status=201)
  return Response(serializer.errors, status=400)

@api_view(['POST'])
def edit_task(request):
  taskId = request.data.get('id')
  try :
    task =  Task.objects.get(id=taskId)
  except:
    return Response({'error': 'Task not found'}, status=404)
  
  serializer = TaskSerializer(task, data=request.data , partial=True)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_task(request ,pk):

  try :
    task =  Task.objects.get(id=pk)
  except:
    return Response({'error': 'Task not found'}, status=404)
  
  if task.status == 'TODO':
    task.status = 'DONE'
  else:
    task.status = 'TODO'
  task.save()
  serializer = TaskSerializer(task)
  return Response(serializer.data)


@api_view(['DELETE'])
def delete_task(request,pk):
  try :
    task =  Task.objects.get(id=pk)
  except:
    return Response({'error': 'Task not found'}, status=404)
  
  task.delete()
  return Response(status=204)

  
  

