from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Login, Student
from django.core.exceptions import *

def index(request):
    return render(request, 'login.html')

def search(request):
    if request.method == 'POST':
        userName = request.POST.get('user', None)
        password = request.POST.get('password', None)
        try:
            user = Login.objects.get(StudentId = userName,password=password)
            #do something with user
            html = ("<H1>Success!</H1>", user)
            return HttpResponse(html)
        except Login.DoesNotExist:
            return HttpResponse("No such user!")
    else:
        return render(request, 'login.html')


def regist(request):
    if request.method == 'POST':
        Uid = request.POST.get('uid',None)
        FName = request.POST.get('fname', None)
        LName = request.POST.get('lname', None)
        Password =request.POST.get('pw', None)
        Degree=request.POST.get('Degree', None)
        Dis = request.POST.get('Discipline', None)
        GDate = request.POST.get('Gratuation Date', None)
        try:
            user = Student.objects.get(FirstName=FName, LastName=LName)
            # do something with user
            html = ("<H1>User already exsit!</H1>", user)
            return HttpResponse(html)
        except Student.DoesNotExist:
            test1=Student(studentId=Uid,FirstName=FName,LastName=LName,Degree=Degree,Discipline=Dis,graduation_year=GDate)
            test2=Login(StudentId=Uid,password=Password)
            test1.save()
            test2.save()
            return HttpResponse("Regist Success!")
    else:
        return render(request, 'signup.html')