from rest_framework import viewsets
from .models import Task
from todo.serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

