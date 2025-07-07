from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

# courses edit and delete 

    path('CoursesApi/', views.CoursesApi.as_view(), name='Courses-list-create'),
    path('CoursesApi/<int:id>/', views.CoursesApi.as_view(), name='Courses-detail-update-delete'),

# college edit and delete    

    path('CollegeApi/', views.CollegeApi.as_view(), name='College-list-create'),
    path('CollegeApi/<int:id>/', views.CollegeApi.as_view(), name='College-detail-update-delete'),

# University edit and delete    

    path('UniversityApi/', views.UniversityApi.as_view(), name='University-list-create'),
    path('UniversityApi/<int:id>/', views.UniversityApi.as_view(), name='University-detail-update-delete'),

# UniversityCourses edit and delete    

    path('UniversityCoursesApi/', views.UniversityCoursesApi.as_view(), name='UniversityCourses-list-create'),
    path('UniversityCoursesApi/<int:id>/', views.UniversityCoursesApi.as_view(), name='UniversityCourses-detail-update-delete'),


    path('CoursesApi/', views.CoursesApi.as_view(), name='Courses'),
    
    path('UniversityApi/', views.UniversityApi.as_view(), name='University'),
    path( 'UniversityCoursesApi/', views.UniversityCoursesApi.as_view(),name= 'UniversityCoursesApi'),
    path('CollegeApi/',views.CollegeApi.as_view(),name='CollegeApi'),
    path('ContactApi/',views.ContactApi.as_view(), name='ContactApi/'),
    
    ]