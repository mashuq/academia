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
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('sessions_by_course/', views.list_sessions_by_course),
    path('sections_by_course/', views.list_sections_by_course),
    path('audio_lessons_by_session/', views.list_audio_lessons_by_session),
    path('video_lessons_by_session/', views.list_video_lessons_by_session),
    path('note_lessons_by_session/', views.list_note_lessons_by_session),
    path('list_mcq_by_session/', views.list_mcq_by_session),
    path('list_sq_by_session/', views.list_sq_by_session),
    path('list_bq_by_session/', views.list_bq_by_session),
    path('list_session_section/', views.list_session_section),
    path('save_session_section_visibility/',
         views.save_session_section_visibility),
    path('register/', views.register),
    path('appoint/', views.appoint)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
