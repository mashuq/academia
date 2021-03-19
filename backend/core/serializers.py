from core.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_polymorphic.serializers import PolymorphicSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        roles = []
        if self.user.is_superuser:
            roles.append('admin')
        student = len(Student.objects.filter(user=self.user))
        if student > 0:
            roles.append("student")
        teacher = len(Teacher.objects.filter(user=self.user))
        if teacher > 0:
            roles.append("teacher")
        data.update({'roles': roles})
        return data


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'testimonial', 'name', 'identity', 'serial', 'visible']


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'name']


class CourseListSerializer(serializers.ModelSerializer):
    course_category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'course_category']


class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class SectionListSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(many=False)

    class Meta:
        model = Section
        fields = ['id', 'name', 'course', 'course_id']


class SectionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class SessionSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSection
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'session']


class AudioLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioLesson
        fields = ['embed', 'audio_type'] + LessonSerializer.Meta.fields


class VideoLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLesson
        fields = ['link', 'video_type'] + LessonSerializer.Meta.fields


class NoteLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteLesson
        fields = ['note'] + LessonSerializer.Meta.fields


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, allow_blank=False, trim_whitespace=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        max_length=20, allow_blank=False, trim_whitespace=True)
    name = serializers.CharField(
        max_length=128, allow_blank=False, trim_whitespace=True)
    email = serializers.EmailField(
        allow_blank=False, validators=[UniqueValidator(queryset=User.objects.all())])
    gender = serializers.ChoiceField(
        choices=['MALE', 'FEMALE'], allow_blank=False)
    date_of_birth = serializers.DateTimeField()


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = '__all__'


class ShortQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortQuestion
        fields = '__all__'


class BroadQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadQuestion
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'date_joined', 'username']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'name', 'gender', 'date_of_birth', 'user']


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'gender', 'date_of_birth',
                  'user', 'biography', 'profile_picture', 'teacher_type']


class TeacherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'name']

class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name']


class SectionTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = SectionTeacher
        fields = ['section', 'teacher']


class SectionTeacherListSerializer(serializers.ModelSerializer):
    section = SectionListSerializer()
    teacher = TeacherListSerializer()

    class Meta:
        model = SectionTeacher
        fields = ['id', 'section', 'teacher']

class EnrolmentListSerializer(serializers.ModelSerializer):
    section = SectionListSerializer()
    student = StudentListSerializer()

    class Meta:
        model = Enrolment
        fields = ['id', 'section', 'student']


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionPolymorpicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MultipleChoiceQuestion: MultipleChoiceQuestionSerializer,
        ShortQuestion: ShortQuestionSerializer,
        BroadQuestion: BroadQuestionSerializer,
        Question: QuestionSerializer
    }


class AssessmentQuestionSerializer(serializers.ModelSerializer):
    question = QuestionPolymorpicSerializer()
    multipleChoiceQuestion = MultipleChoiceQuestionSerializer()

    class Meta:
        model = AssessmentQuestion
        fields = ['question', 'multipleChoiceQuestion']

class EnrolmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrolment
        fields = '__all__'