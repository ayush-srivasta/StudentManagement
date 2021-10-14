from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import Case

# Create your models here.


class CustomBaseuser(AbstractUser):
    
    TYPES = (
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    )

    user_type = models.CharField(choices=TYPES, max_length=10,blank=False)
    phoneNo=models.CharField(max_length=10,blank=True)


class Subject(models.Model):
 name = models.CharField(max_length=255)
 marks=models.ForeignKey(to="Marks",on_delete=CASCADE,null=True)
 teacher=models.ManyToManyField(to="TeacherProfile",related_name='teacher')
 def __str__(self):
     return self.name
 
class Year(models.Model):
    yearName=models.CharField(max_length=20)
    def __str__(self):
     return self.yearName

class Department(models.Model):
    depName=models.CharField(max_length=20)
    def __str__(self):
     return self.depName

                              

class StudentProfile(CustomBaseuser):
    isCompleted=models.BooleanField(default=False)
    roll_no = models.CharField(max_length=20,blank=True)
    subject = models.ManyToManyField(to=Subject, related_name='students')
    year=models.ForeignKey(Year,on_delete=models.SET_NULL,null=True)
    dept = models.ForeignKey(to=Department,on_delete=models.SET_NULL,blank=True,null=True,related_name='students')
    class Meta:
        verbose_name="Student"
        verbose_name_plural="Student"
    def __str__(self):
      return self.username

      
class TeacherProfile(CustomBaseuser):
    isCompleted=models.BooleanField(default=False)
    year=models.ForeignKey(Year,on_delete=models.SET_NULL,null=True)
    subject = models.ManyToManyField(to=Subject, related_name='teachers')
    class Meta:
        verbose_name="Teacher"
        verbose_name_plural="Teacher"
    def __str__(self):
     return self.username

class Marks(models.Model):
    student_id=models.ForeignKey(StudentProfile,on_delete=CASCADE,null=True)
    subject_id=models.ForeignKey(to=Subject,on_delete=CASCADE,null=True,related_name='sub_id')
    ta1=models.IntegerField(default=0)
    ta2=models.IntegerField(default=0)
    ta3=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.student_id.username+" "+str(self.subject_id)



