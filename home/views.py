from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib import messages
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
def index(request):
    return render(request, "index.html")

#-----------------------------ApiViews ---------------------#

class CoursesApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = Courses.objects.all()
        serializer = CoursesSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
            
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            data = Courses.objects.get(id=id)
        except Courses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CoursesSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:
            data = Courses.objects.get(id=id)
        except Courses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UniversityApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = University.objects.all()
        serializers = UniversitySerializer(data,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK) 
    
    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            data = University.objects.get(id=id)
        except University.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UniversitySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:
            data = University.objects.get(id=id)
        except University.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UniversityCoursesApi(APIView):
    permission_classes = [AllowAny] 

    def get(self, request):
        data = UniversityCourses.objects.all()
        serializers = UniversityCoursesSerializer(data,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = UniversityCoursesPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            data = UniversityCourses.objects.get(id=id)
        except UniversityCourses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UniversityCoursesPostSerializer(data, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:
            data = UniversityCourses.objects.get(id=id)
        except UniversityCourses.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CollegeApi(APIView):
    permission_classes = [AllowAny] 
    def get(self, request):
        data = College.objects.all()
        serializers = CollegeSerializer(data,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
        
    def post(self, request):
        serializer = CollegePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            data = College.objects.get(id=id)
        except College.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CollegePostSerializer(data, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            data = College.objects.get(id=id)
        except College.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

     
class ContactApi (APIView):
    permission_classes=[AllowAny]
    def get(self,requast):
        data = Contact.objects.all()
        serializer = ContactSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#-----------datacreating------------*  
  
    def post(self,request):
        serializer = ContactPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)