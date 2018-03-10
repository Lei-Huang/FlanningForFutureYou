from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from django.core.exceptions import *

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def log(request):
    return render(request, 'test.html')

def search(request):
    context = {}
    if request.method == 'POST':
        userName = request.POST.get('user', None)
        password = request.POST.get('password', None)
        try:
            user = Login.objects.get(StudentId = userName,password=password)
            #do something with user
            #html = (userName,"<H1>Success!</H1>")
            #context['userName'] = userName
            request.session['userName'] = userName
            return render(request,'index.html')
            #return HttpResponse(html)
        except Login.DoesNotExist:
            return render(request, 'login_fail.html')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        Uid = request.POST.get('uid',None)
        FName = request.POST.get('fname', None)
        LName = request.POST.get('lname', None)
        Password =request.POST.get('pw', None)
        Degree=request.POST.get('Degree', None)
        Dis = request.POST.get('Discipline', None)
        GDate = request.POST.get('Graduation Date', None)
        context = {}
        context['userid'] = Uid
        try:
            # Todo use uid to check whether user exist
            user = Student.objects.get(studentId=Uid)
            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'UserExist.html',context)
        except Student.DoesNotExist:
            test1=Student(studentId=Uid,FirstName=FName,LastName=LName,Degree=Degree,Discipline=Dis,graduation_year=GDate)
            test2=Login(StudentId=Uid,password=Password)
            test1.save()
            test2.save()
            #return render(request, 'login.html')
            return render(request,'register_success.html')
    else:
        return render(request, 'signup.html')


def current_profile(request):
    if request.method == 'POST':
        user1 = request.POST.get('user',None)
        Study_year= request.POST.get('password', None)
        Work = request.POST.get('work', None)
        Volunteer =request.POST.get('volunteer', None)
        Detail_work=request.POST.get('detail_work', None)
        Detail_vol = request.POST.get('detail_vol', None)
        context = {}
        context['userid'] = Uid
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            user.YearOfStudy=Study_year
            user.save(update_fields=['YearOfStudy'])
            test2 = UserProfile(StudentId=Major,Work_exp=Work, Volunteer_exp=Volunteer,Detail_work=Detail_work, Detail_volunteer=Detail_vol)
            test2.save()
            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'test2.html')
        except Student.DoesNotExist:
            #return render(request, 'login.html')
            return render(request,'index.html')
    else:
        return render(request, 'test2.html')
