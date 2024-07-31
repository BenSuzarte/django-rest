from rest_framework import generics, status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

from rest_framework.views import APIView

# Create your views here.
class TaskPostListCreate(generics.ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

  def delete(self, request, *args, **kwargs):
    Task.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class TaskPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  lookup_field = 'pk'

class TaskPostList(APIView):
  def get(self, request, format=None):
    title = request.query_params.get('title', '')

    if title:
      tasks = Task.objects.filter(title__icontains=title)
    else:
      tasks = Task.objects.all()

    serializer = Task(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)