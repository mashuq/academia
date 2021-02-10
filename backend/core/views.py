from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import *
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt import views as jwt_views


class CustomTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('serial')
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all().order_by('id')
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseRetrieveSerializer 

    queryset = Course.objects.all().select_related(
        'course_category').order_by('id')
    permission_classes = [permissions.IsAuthenticated]


class SectionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return SectionListSerializer
        return SectionRetrieveSerializer

    queryset = Section.objects.all().select_related(
        'course').order_by('id')
    permission_classes = [permissions.IsAuthenticated]

