"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, path
from rest_framework import routers
from core import views
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'course_categories', views.CourseCategoryViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'sections', views.SectionViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'audio_lessons', views.AudioLessonViewSet)
router.register(r'video_lessons', views.VideoLessonViewSet)
router.register(r'note_lessons', views.NoteLessonViewSet)
router.register(r'link_lessons', views.LinkLessonViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'mcq', views.MultipleChoiceQuestionViewSet)
router.register(r'bq', views.BroadQuestionViewSet)
router.register(r'sq', views.ShortQuestionViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'section_teachers', views.SectionTeacherViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('sessions_by_course/', views.list_sessions_by_course),
    path('sections_by_course/', views.list_sections_by_course),
    path('audio_lessons_by_session/', views.list_audio_lessons_by_session),
    path('video_lessons_by_session/', views.list_video_lessons_by_session),
    path('note_lessons_by_session/', views.list_note_lessons_by_session),
    path('link_lessons_by_session/', views.list_link_lessons_by_session),
    path('list_mcq_by_session/', views.list_mcq_by_session),
    path('list_sq_by_session/', views.list_sq_by_session),
    path('list_bq_by_session/', views.list_bq_by_session),
    path('list_session_section/', views.list_session_section),
    path('save_session_section_visibility/',
         views.save_session_section_visibility),
    path('register/', views.register),
    path('appoint/', views.appoint),
    path('password_reset/', views.password_reset),     
    path('list_sections_for_teacher/', views.list_sections_for_teacher),
    path('list_assessment_for_teacher/', views.list_assessment_for_teacher),
    path('save_assessment_for_teacher/', views.save_assessment_for_teacher),
    path('save_assessment_question_for_teacher/',
         views.save_assessment_question_for_teacher),
    path('list_assessment_question_for_teacher/',
         views.list_assessment_question_for_teacher),
    path('delete_assessment_question_for_teacher/',
         views.delete_assessment_question_for_teacher),
    path('get_student_section/',
         views.get_student_section),
    path('save_enrolment/',
         views.save_enrolment),
    path('delete_enrolment/',
         views.delete_enrolment),
    path('home_testimonials/',
         views.home_testimonials),
    path('list_sections_for_student/',
         views.list_sections_for_student),
    path('list_detailed_sections_for_teacher/',
         views.list_detailed_sections_for_teacher), 
    path('list_sections_for_teacher/',
         views.list_sections_for_teacher), 
    path('sessions_by_course_student/',
         views.sessions_by_course_student),
    path('sessions_by_course_teacher/',
         views.sessions_by_course_teacher),
    path('audio_lessons_by_session_student/',
         views.audio_lessons_by_session_student),
    path('video_lessons_by_session_student/',
         views.video_lessons_by_session_student),
    path('note_lessons_by_session_student/',
         views.note_lessons_by_session_student),
    path('link_lessons_by_session_student/',
         views.link_lessons_by_session_student),
    path('audio_lessons_by_session_teacher/',
         views.audio_lessons_by_session_teacher),
    path('video_lessons_by_session_teacher/',
         views.video_lessons_by_session_teacher),
    path('note_lessons_by_session_teacher/',
         views.note_lessons_by_session_teacher),
    path('link_lessons_by_session_teacher/',
         views.link_lessons_by_session_teacher), 
    path('search_student/',
         views.search_student),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
