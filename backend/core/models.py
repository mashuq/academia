from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


class Testimonial(models.Model):
    testimonial = models.CharField(max_length=4000)
    name = models.CharField(max_length=64)
    identity = models.CharField(max_length=128)
    serial = models.IntegerField()
    visible = models.BooleanField()


class CourseCategory(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=10)
    description = models.TextField()
    curriculum = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='course_images/')
    visible = models.BooleanField()
    course_category = models.ForeignKey(
        'CourseCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    visible = models.BooleanField()


class Session(models.Model):
    name = models.CharField(max_length=512)
    serial = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)


class SessionSection(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    visible = models.BooleanField()

    class Meta:
        unique_together = [['section', 'session']]


class Lesson(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(null=True, blank=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)


class VideoLesson(Lesson):
    class VideoType(models.TextChoices):
        YOUTUBE = 'YOUTUBE', _('YouTube')
    link = models.CharField(max_length=512)
    video_type = models.CharField(
        choices=VideoType.choices, default=VideoType.YOUTUBE, max_length=32)


class AudioLesson(Lesson):
    class AudioType(models.TextChoices):
        SOUNDCLOUD = 'SOUNDCLOUD', _('SoundCloud')
    embed = models.TextField()
    audio_type = models.CharField(
        choices=AudioType.choices, default=AudioType.SOUNDCLOUD, max_length=32)


class NoteLesson(Lesson):
    note = models.FileField(upload_to="course_files/")


class LinkLesson(Lesson):
    title = models.CharField(max_length=512)
    link = models.CharField(max_length=512)

class Assessment(models.Model):
    name = models.CharField(max_length=256)
    contribution = models.FloatField()
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    quiz = models.ForeignKey('Quiz', null=True, blank=True, on_delete=models.CASCADE)

class Quiz(models.Model):
    name = models.CharField(max_length=256)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    contribution = models.FloatField()

class Question(PolymorphicModel):
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    mark = models.FloatField()

class AssessmentQuestion(models.Model):
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['assessment', 'question']]

class QuizQuestion(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['quiz', 'question']]

class AssessmentResult(models.Model):
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE)
    total_mark = models.FloatField()
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

class Answer(models.Model):
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE)
    mark = models.FloatField()
    student = models.ForeignKey('Student', on_delete=models.CASCADE)


class MultipleChoiceAnswer(Answer):
    answer = models.CharField(max_length=128)


class ShortAnswer(Answer):
    answer = models.CharField(max_length=2048)


class BroadAnswer(Answer):
    answer = models.TextField()


class MultipleChoiceQuestion(Question):
    question = models.CharField(max_length=512)
    choice1 = models.CharField(max_length=128)
    choice2 = models.CharField(max_length=128)
    choice3 = models.CharField(max_length=128)
    choice4 = models.CharField(max_length=128)
    correct_choice = models.CharField(max_length=128)


class ShortQuestion(Question):
    question = models.CharField(max_length=512)


class BroadQuestion(Question):
    question = models.CharField(max_length=512)


class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', _('Male')
        FEMALE = 'FEMALE', _('Female')

    name = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=Gender.choices, max_length=6)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return name


class Enrolment(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    final_grade = models.FloatField()

    class Meta:
        unique_together = [['section', 'student']]


class Teacher(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', _('Male')
        FEMALE = 'FEMALE', _('Female')

    class TeacherType(models.TextChoices):
        MAIN = 'MAIN', _('Main')
        ASSISTANT = 'ASSISTANT', _('Assistant')

    name = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=Gender.choices, max_length=6)
    date_of_birth = models.DateTimeField(null=True)
    biography = models.TextField(null=True)
    profile_picture = models.ImageField(null=True)
    teacher_type = models.CharField(choices=TeacherType.choices, max_length=32)


class SectionTeacher(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['section', 'teacher']]


class Admin(models.Model): 
    name = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
