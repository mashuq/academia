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
    idx = serializers.SerializerMethodField()
    def get_idx(self, obj):
        return obj.id
    class Meta:
        model = CourseCategory
        fields = ['id', 'name', 'idx']

class CourseListSerializer(serializers.ModelSerializer):
    idx = serializers.SerializerMethodField()
    def get_idx(self, obj):
        return obj.id
    class Meta:
        model = Course
        fields = ['id', 'name', 'idx', 'course_category']

class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
          



