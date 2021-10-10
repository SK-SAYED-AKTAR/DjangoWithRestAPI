from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import StudentClass
from .serializers import StudentSerializer

# Create your views here.

class StudentView(ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentSerializer