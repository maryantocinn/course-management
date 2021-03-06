from rest_framework import viewsets

from courses_api import serializers
from courses_api import models

class CourseViewSet(viewsets.ModelViewSet):
  """Handle Course Nested CRUD"""
  serializer_class = serializers.CourseSerializer
  queryset = models.Course.objects.all()


class LessonViewSet(viewsets.ModelViewSet):
  """Handle Lesson CRUD"""
  serializer_class = serializers.LessonSerializer
  queryset = models.Lesson.objects.all()


class MaterialViewSet(viewsets.ModelViewSet):
  """Handle Material CRUD"""
  serializer_class = serializers.MaterialSerializer
  queryset = models.Material.objects.all()


class IndividualCourseViewSet(viewsets.ModelViewSet):
  """Handle Course only CRUD"""
  serializer_class = serializers.IndividualCourseSerializer
  queryset = models.Course.objects.all()