from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=80)
    rollnumber = models.IntegerField(unique=True)
    student_class = models.IntegerField()
    student_age = models.IntegerField()
    reg_no = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return f"{self.student_name} : {self.rollnumber}"

class Teacher(models.Model):
    tech_name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')
