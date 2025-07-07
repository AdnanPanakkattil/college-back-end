from django.db import models

# Create your models here.
       
class Courses(models.Model):
    courses_name = models.CharField(max_length=200 ,null=True ,blank=True)


    def __str__(self):
        return self. courses_name
    

class University(models.Model):
    University_name = models.CharField(max_length=200 ,null=True , blank=True)
    image = models.ImageField(upload_to='University/', null=True, blank=True)

class UniversityCourses(models.Model):
    courseid = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    University_id = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)

 
class College(models.Model):
    
    College_name = models.CharField(max_length=200 ,null=True ,blank=True)
    Place = models.CharField(max_length=200 , null=True , blank=True)
    state = models.CharField(max_length=200,null=True , blank=True)
    University_id = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self. College_name


class Contact(models.Model):

    Name = models.CharField(max_length=255,null=True, blank=True)
    Age = models.CharField(max_length=255,null=True,blank=True)
    Phone_number = models.CharField(max_length=255,null=True,blank=True)
    College_name = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    courses_name = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
