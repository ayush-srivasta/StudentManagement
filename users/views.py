from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .import models
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    error_msg=""
    if request.method == 'POST':
       
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_msg="Username or password is incorrect"
    return render(request,'users/loginPage.html',{'error':error_msg})

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        phoneNo=request.POST.get('phoneNo')
        password=request.POST.get('password')
        userType=request.POST.get('usertype')
        if userType == 'Teacher':
            obj=models.TeacherProfile.objects.create(username=username,first_name=first_name,last_name=last_name,phoneNo=phoneNo,email=email,user_type=userType)
            obj.set_password(password)
            obj.save()
        elif userType=='Student':
            obj=models.StudentProfile.objects.create(username=username,first_name=first_name,last_name=last_name,phoneNo=phoneNo,email=email,user_type=userType)
            obj.set_password(password)
            obj.save() 
    return render(request,'users/signUp.html')

@login_required
def home(request):
    isTeacher=False
    name=request.user.username
    print(name)
    userType=request.user.user_type
    print(userType)
    if userType == "Teacher":
        isTeacher=True
       
        year=models.Year.objects.all()
        obj=models.TeacherProfile.objects.get(username=request.user.username)
        subject=models.Subject.objects.all()
        
        if  not(obj.isCompleted):
            return render(request,'users/home.html',{'year':year,'subject':subject, 'teacher':isTeacher,'name':name})
    else:
        obj=models.StudentProfile.objects.get(username=request.user.username)
        department=models.Department.objects.all()
        year=models.Year.objects.all()
        if not(obj.isCompleted):
            return render(request,'users/home.html',{'year':year,'department':department, 'teacher':isTeacher,'name':name})
    return redirect('main')

@login_required    
def main(request):
    name=request.user.username
    
    if request.user.user_type=='Student':
        student=models.StudentProfile.objects.get(username=request.user.username)
        subject=student.subject.all()
        return render(request,'users/main.html',{'name':name,'subject':subject})
    else:
        teacher=models.TeacherProfile.objects.get(username=request.user.username)
        subject=teacher.subject.all()
        print(subject)
        return render(request,'users/teacherInfo.html',{'name':name,'subject':subject})


@login_required
def Logout(request):
    logout(request)
    return redirect('login')

def verify(request):
    if request.user.user_type == 'Teacher':
       
        teacher=models.TeacherProfile.objects.get(username=request.user.username)
        for item in request.POST.getlist('subject'):
            teacher.subject.add(models.Subject.objects.get(name=item))
        teacher.year=models.Year.objects.get(yearName=request.POST.get('year'))
        teacher.isCompleted=True
        teacher.save()
    else:
         student=models.StudentProfile.objects.get(username=request.user.username)
         student.roll_no=request.POST.get('roolno')
         student.year=None
         student.year=models.Year.objects.get(yearName=request.POST.get('year'))
         student.dept=models.Department.objects.get(depName=request.POST.get('department'))
        
         selectSubject(request.user.username,student.dept.depName)
         student.isCompleted=True
         student.save()
    return redirect('main')

def selectSubject(username,depName):
    student=models.StudentProfile.objects.get(username=username)
    
    if depName == "Computer Science":
        student.subject.add(models.Subject.objects.get(name="DS"))
      
        student.subject.add(models.Subject.objects.get(name="DBMS"))
        student.subject.add(models.Subject.objects.get(name="ADSA"))
    elif depName =="Chemical":
        student.subject.add(models.Subject.objects.get(name="Chemistry"))

@login_required
def subject(request,str):
    
    name=request.user.username
    student=models.StudentProfile.objects.get(username=request.user.username)
    subject=student.subject.get(name=str)
    marks=subject.marks
    
    if marks == None:
        marks=models.Marks.objects.get_or_create(student_id=student,subject_id=subject)
    return render(request,'users/marks.html',{'name':name,'subject':subject,'marks':marks[0]})

@login_required
def stuList(request,str):
    name=request.user.username
    student=models.StudentProfile.objects.filter(subject=models.Subject.objects.get(name=str))
    return render(request,'users/studentList.html',{'name':name, 'student':student,'subject':str})

@login_required
def subjectTeacher(request,str,subject):
    name=request.user.username
    print(name)
    teaher=models.TeacherProfile.objects.get(username=name)   
    student=models.StudentProfile.objects.get(username=str)
    subject=student.subject.get(name=subject)
    try:
        marks=models.Marks.objects.get(student_id=student,subject_id=subject)
        if request.method == 'POST':
            ta1=request.POST.get('ta1')
            ta2=request.POST.get('ta2')
            ta3=request.POST.get('ta3')
            marks.ta1=ta1
            marks.ta2=ta2
            marks.ta3=ta3
            marks.save()
    except models.Marks.DoesNotExist:
        marks=models.Marks.objects.create(student_id=student,subject_id=subject)
    return render(request,'users/subjectTeacher.html',{'name':name,'subject':subject,'marks':marks,'student':str})
