from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework.response import Response


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
