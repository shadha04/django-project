from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    usertype=models.CharField(max_length=20)

class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    confirm_password=models.CharField(max_length=20)
    address=models.TextField(max_length=200)
    phno=models.IntegerField()
    salary=models.IntegerField()
    experience=models.IntegerField()

class Student(models.Model):
    student_id=models.ForeignKey(User,on_delete=models.CASCADE)
    confirm_password=models.CharField(max_length=20)
    address=models.TextField(max_length=200)
    phno=models.IntegerField()
    image=models.ImageField(upload_to='uploads', null=True,blank=True)
    guardian=models.CharField(max_length=20)

