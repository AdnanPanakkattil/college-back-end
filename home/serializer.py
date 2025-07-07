from rest_framework import serializers
from .models import *


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields ='__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields ='__all__'


class UniversityCoursesSerializer(serializers.ModelSerializer):

    courseid= CoursesSerializer()
    University_id=UniversitySerializer()

    class Meta:
        model = UniversityCourses
        fields = '__all__'

class UniversityCoursesPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UniversityCourses
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    University_id =UniversitySerializer()
    class Meta:
        model = College
        fields = '__all__'


class CollegePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    College_name = CollegeSerializer()
    courses_name = CoursesSerializer()
    
    class Meta:
        model = Contact
        fields = '__all__'
        

class ContactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        