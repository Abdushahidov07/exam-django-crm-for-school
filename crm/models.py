from django.db import models

# Create your models here.
class Student(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    grade_level = models.IntegerField()


class Teacher(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField (max_length=50)
    hire_date = models.DateField()



class Classes(models.Model):
    class_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_id = models.IntegerField()
    schedule = models.TextField()

class Enrlloments(models.Model):
    student_id = models.IntegerField()
    class_id = models.IntegerField()
    enrlloments_date = models.DateField()


class Parents(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)


class Student_parents(models.Model):
    student_id = models.IntegerField()
    parents_id = models.IntegerField()



class Grades(models.Model):
    student_id = models.IntegerField()
    class_id = models.IntegerField()
    grades = models.IntegerField()
    grades_date = models.DateField()

class Attendance(models.Model):
    student_id = models.IntegerField()
    class_id = models.IntegerField()
    attendenc_date = models.DateField()
    status = models.BooleanField()

class Messages(models.Model):
    sender_id = models.IntegerField()
    recipient_id = models.IntegerField()
    message = models.TextField() 
    message_date = models.DateField()
    
    

