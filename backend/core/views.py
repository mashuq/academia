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
from django.db import transaction
from django.contrib.auth.hashers import make_password


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


class AudioLessonViewSet(viewsets.ModelViewSet):
    queryset = AudioLesson.objects.all().order_by('id')
    serializer_class = AudioLessonSerializer
    permission_classes = [permissions.IsAdminUser]


class VideoLessonViewSet(viewsets.ModelViewSet):
    queryset = VideoLesson.objects.all().order_by('id')
    serializer_class = VideoLessonSerializer
    permission_classes = [permissions.IsAdminUser]


class NoteLessonViewSet(viewsets.ModelViewSet):
    queryset = NoteLesson.objects.all().order_by('id')
    serializer_class = NoteLessonSerializer
    permission_classes = [permissions.IsAdminUser]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('id')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_sessions_by_course(request):
    sessions = Session.objects.filter(
        course=request.data['course']).order_by('serial')
    serialized_data = SessionSerializer(sessions, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_audio_lessons_by_session(request):
    lessons = AudioLesson.objects.filter(
        session=request.data['session'])
    serialized_data = AudioLessonSerializer(lessons, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_video_lessons_by_session(request):
    lessons = VideoLesson.objects.filter(
        session=request.data['session'])
    serialized_data = VideoLessonSerializer(lessons, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_note_lessons_by_session(request):
    lessons = NoteLesson.objects.filter(
        session=request.data['session'])
    serialized_data = NoteLessonSerializer(lessons, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@transaction.atomic
def register(request):
    serializer = RegistrationSerializer(
        data=request.data)
    serializer.is_valid(raise_exception=True)
    password = make_password(request.data['password'])
    user = User(is_superuser=False, password=password,
                email=request.data['email'], username=request.data['username'], is_active=True, is_staff=False)
    user.save()
    student = Student(date_of_birth=request.data['date_of_birth'],
                      user=user, name=request.data['name'], gender=request.data['gender'])
    student.save()
    return HttpResponse(status=200)
