from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializers
from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializers_class = TaskSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializers_class = TaskSerializers


class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializers_class = TaskSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
