from core.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        roles = []
        if self.user.is_superuser:
            roles.append('admin')
        data.update({'roles': roles})
        return data


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['testimonial', 'name', 'identity', 'serial']


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
        fields = ['id', 'name', 'course']


class SectionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
