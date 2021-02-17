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
from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        if 'page' not in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('serial')
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all().order_by('name')
    serializer_class = CourseCategorySerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class CourseViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseRetrieveSerializer

    queryset = Course.objects.all().select_related(
        'course_category').order_by('name')
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class SectionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return SectionListSerializer
        return SectionRetrieveSerializer

    queryset = Section.objects.all().select_related(
        'course').order_by('name')
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


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
def list_sections_by_course(request):
    sections = Section.objects.filter(
        course=request.data['course']).order_by('id')
    serialized_data = SectionListSerializer(sections, many=True)
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
@permission_classes([permissions.IsAdminUser])
def list_mcq_by_session(request):
    mcq_list = MultipleChoiceQuestion.objects.filter(
        session=request.data['session']).order_by('id')
    page = request.data['page']
    paginator = Paginator(mcq_list, 5)
    try:
        mcqs = paginator.page(page)
    except PageNotAnInteger:
        mcqs = paginator.page(1)
    except EmptyPage:
        mcqs = paginator.page(paginator.num_pages)
    serialized_data = MultipleChoiceQuestionSerializer(mcqs, many=True)
    result = {'result': serialized_data.data, 'count': mcq_list.count()}
    return Response(result)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_sq_by_session(request):
    sq_list = ShortQuestion.objects.filter(
        session=request.data['session']).order_by('id')
    page = request.data['page']
    paginator = Paginator(sq_list, 5)
    try:
        sqs = paginator.page(page)
    except PageNotAnInteger:
        sqs = paginator.page(1)
    except EmptyPage:
        sqs = paginator.page(paginator.num_pages)
    serialized_data = ShortQuestionSerializer(sqs, many=True)
    result = {'result': serialized_data.data, 'count': sq_list.count()}
    return Response(result)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_bq_by_session(request):
    bq_list = BroadQuestion.objects.filter(
        session=request.data['session']).order_by('id')
    page = request.data['page']
    paginator = Paginator(bq_list, 5)
    try:
        bqs = paginator.page(page)
    except PageNotAnInteger:
        bqs = paginator.page(1)
    except EmptyPage:
        bqs = paginator.page(paginator.num_pages)
    serialized_data = BroadQuestionSerializer(bqs, many=True)
    result = {'result': serialized_data.data, 'count': bq_list.count()}
    return Response(result)


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


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@transaction.atomic
def appoint(request):
    serializer = RegistrationSerializer(
        data=request.data)
    serializer.is_valid(raise_exception=True)
    password = make_password(request.data['password'])
    user = User(is_superuser=False, password=password,
                email=request.data['email'], username=request.data['username'], is_active=True, is_staff=False)
    user.save()
    teacher = Teacher(date_of_birth=request.data['date_of_birth'],
                      user=user, name=request.data['name'], gender=request.data['gender'],
                      biography=request.data['biography'], teacher_type=request.data['teacher_type'],
                      profile_picture=request.data['profile_picture'])
    teacher.save()
    return HttpResponse(status=200)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def list_session_section(request):
    session_sections = SessionSection.objects.filter(
        section=request.data['section']).order_by('id')
    serialized_data = SessionSectionSerializer(session_sections, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@transaction.atomic
def save_session_section_visibility(request):
    SessionSection.objects.filter(
        section=request.data['section']).update(visible=False)

    for session_section_data in request.data['visible_list']:
        try:
            serializer = SessionSectionSerializer(data=session_section_data)
            serializer.is_valid(raise_exception=True)
            session_section = SessionSection(
                session=Session.objects.get(
                    pk=session_section_data['session']),
                section=Section.objects.get(
                    pk=session_section_data['section']),
                visible=True)
            session_section.save()
        except Exception as e:
            print(e)
            SessionSection.objects.filter(
                section=session_section_data['section'], session=session_section_data['session']).update(visible=True)

    return HttpResponse(status=200)


class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceQuestion.objects.all().order_by('question')
    serializer_class = MultipleChoiceQuestionSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class ShortQuestionViewSet(viewsets.ModelViewSet):
    queryset = ShortQuestion.objects.all().order_by('question')
    serializer_class = ShortQuestionSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class BroadQuestionViewSet(viewsets.ModelViewSet):
    queryset = BroadQuestion.objects.all().order_by('question')
    serializer_class = BroadQuestionSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('user').order_by('name')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.user.delete()
            self.perform_destroy(instance)
        except Http404:
            pass

        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related('user').order_by('name')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.user.delete()
            self.perform_destroy(instance)
        except Http404:
            pass

        return Response(status=status.HTTP_204_NO_CONTENT)
