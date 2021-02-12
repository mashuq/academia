from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from rest_framework import viewsets
from rest_framework import authentication, permissions
from core.serializers import *
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt import views as jwt_views
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class CustomTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('serial')
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all().order_by('id')
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CourseViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseRetrieveSerializer

    queryset = Course.objects.all().select_related(
        'course_category').order_by('id')
    permission_classes = [permissions.IsAdminUser]


class SectionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return SectionListSerializer
        return SectionRetrieveSerializer

    queryset = Section.objects.all().select_related(
        'course').order_by('id')
    permission_classes = [permissions.IsAdminUser]


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('serial')
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_sessions_by_course(request):
    sessions = Session.objects.filter(course=request.data['course'])
    serialized_data = SessionSerializer(sessions, many=True)
    return Response(serialized_data.data)
