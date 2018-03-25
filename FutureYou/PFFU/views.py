from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from django.core.exceptions import *

# use session to keep user loginin, distinguished by username
def index(request):
    if request.method == 'GET':
        context['username'] = request.session['userName']

        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')

# def portfolio(request):
#         return render(request, 'portfolio.html')

# retrieve user profile detail from database
def profile(request):
    if request.method == 'GET':
        context = {}
        try:
            # check session that if any current user has been login            
            user = Student.objects.get(studentId=request.session['userName'])
            userProfile = UserProfile.objects.get(StudentId=user)
            context['Uid'] = user.studentId
            context['Lastname'] = user.LastName
            context['Firstname']=user.FirstName
            context['Dis']=user.Discipline
            context['degree'] = user.Degree
            context['exp'] =  userProfile.Work_exp
            context['skill']=userProfile.Detail_work
            context['vol']=userProfile.Volunteer_exp
            context['detail_vol'] = userProfile.Detail_volunteer
            context['program'] = userProfile.FirstProgram
            context['program2'] = userProfile.SecondProgram
            context['major'] = userProfile.FirstMajor
            context['major2'] = userProfile.SecondMajor

            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'portfolio_subpages/profile.html',context)
        except Student.DoesNotExist:
            #return render(request, 'login.html')
            return render(request,'index.html')
    else:
            return render(request, 'portfolio_subpages/profile.html')

def workshops(request):
    return render(request, 'portfolio_subpages/workshops.html')


def understanding_yourself(request):
    return render(request, 'portfolio_subpages/understanding_yourself.html')

def employability_skill(request):
    return render(request, 'portfolio_subpages/employability_skill.html')

def future_skill(request):
    return render(request, 'portfolio_subpages/future_skill.html')

def uy_yes(request):
    return render(request, 'portfolio_subpages/uy_yes.html')

def uy_choice1(request):
    return render(request, 'portfolio_subpages/uy_choice1.html')

def uy_choice2(request):
    return render(request, 'portfolio_subpages/uy_choice2.html')

def research_employer(request):
    return render(request, 'portfolio_subpages/research_employer.html')


def interview_skill(request):
    return render(request, 'portfolio_subpages/interview_skill.html')


def career_goal(request):
    return render(request, 'portfolio_subpages/career_goal.html')


def log(request):
    return render(request, 'test.html')


def current_profile(request):
    if request.method == 'POST':
        sector = request.POST.get('cg_industry',None)
        firstRole = request.POST.get('firstgoal', None)
        secondRole = request.POST.get('secondgoal', None)
        thirdRole = request.POST.get('thirdgoal', None)
        FirstPlan= request.POST.get('cg_q1',None)
        SecondPlan = request.POST.get('cg_q2', None)
        ThirdPlan =request.POST.get('cg_q3', None)
        context = {}
        #context['userid'] = Uid
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            userPro=CareerGoal.objects.get(StudentId=user)
            return render(request,'portfolio_subpages/career_goal.html')

        except UserProfile.DoesNotExist:
            user = Student.objects.get(studentId=request.session['userName'])
            #user.YearOfStudy=Study_year
            #user.save(update_fields=['YearOfStudy'])
            progress2=ProgressionBar.objects.get(StudentId=user)
            progress2.CurrentProgress=2
            progress2.save(update_fields=['CurrentProgress'])
            #if Volunteer==None:
             #   Volunteer="no"
            test2 = CareerGoal(StudentId=user,Sector=sector,FirstRow=firstRole, SecondRow=secondRole,ThirdRow=thirdRole,FirstPlan=FirstPlan,SecondPlan=SecondPlan,ThirdPlan=ThirdPlan)
            test2.save()

            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'portfolio.html')
            #return render(request, 'login.html')
    else:
        return render(request, 'portfolio_subpages/career_goal.html')

#use an integer to tell user which step they are currently at
def progress(request):
    context1 = {}
    if request.method == 'GET':
        try:
             user = Login.objects.get(StudentId=request.session.get('userName',None))
             user2= Student.objects.get(studentId=request.session['userName'])
             progression= ProgressionBar.objects.get(StudentId=user2)
             context1['progressInt'] = int(progression.CurrentProgress)
             return render(request, 'portfolio.html',context1)
        except Login.DoesNotExist:
            return render(request, 'Needlogin.html')
    else:
        return render(request, 'login.html')


def search(request):
    context1 = {}
    if request.method == 'POST':
        userName = request.POST.get('user', None)
        password = request.POST.get('password', None)
        try:
            user = Login.objects.get(StudentId = userName,password=password)
            #do something with user
            #html = (userName,"<H1>Success!</H1>")
            #context['userName'] = userName
            request.session['userName'] = userName
            # user logging in expiry time by seconds 
            request.session.set_expiry(3600)
            context1['userName'] = request.session['userName']
            #request.session.clear()
            return render(request,'index.html',context1)
            #return HttpResponse(html)
        except Login.DoesNotExist:
            return render(request, 'login_fail.html')
    else:
        return render(request,'login.html')



def logout(request):
    context2 = {}
    if request.method == 'POST':
            #clear the session, return to index page.
            request.session.clear()
            context2['userName'] = 1
            return render(request,'index.html',context2)
            #return HttpResponse(html)
    else:
        #request.session.clear()
        return render(request,'index.html')

# user create account with their basic information, save data into database.
def register(request):
    if request.method == 'POST':
        Uid = request.POST.get('uid',None)
        FName = request.POST.get('fname', None)
        LName = request.POST.get('lname', None)
        Password =request.POST.get('pw', None)
        # todo: change degree into drop down menu?
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
            test1 = Student(studentId=Uid,FirstName=FName,LastName=LName,Degree=Degree,Discipline=Dis,graduation_year=GDate)
            test2 = Login(StudentId=Uid,password=Password)
            test3 = ProgressionBar(StudentId=test1,CurrentProgress=0)
            test1.save()
            test2.save()
            test3.save()
            #return render(request, 'login.html')
            return render(request,'register_success.html')
    else:
        return render(request, 'signup.html')

# retrieve user current profile detail from database,
# save new or update existing profile information, and save into database 
def current_profile(request):
    if request.method == 'GET':
        context = {}
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            userProfile = UserProfile.objects.get(StudentId=user)
            context['Uid'] = user.studentId
            context['Lastname'] = user.LastName
            context['Firstname']=user.FirstName
            context['Dis']=user.Discipline
            context['degree'] = user.Degree
            context['exp'] =  userProfile.Work_exp
            context['skill']=userProfile.Detail_work
            context['detail_vol'] = userProfile.Detail_volunteer
                    # do something with user
                    #html = ("<H1>User already exsit!</H1> ")
            userPro=UserProfile.objects.get(StudentId=user)
            return render(request,'portfolio_subpages/profile.html',context)
        except UserProfile.DoesNotExist:
            return render(request,'current_profile.html')

    if request.method == 'POST':
        program = request.POST.get('program',None)
        program2 = request.POST.get('program2', None)
        major = request.POST.get('major', None)
        major2 = request.POST.get('major2', None)
        Study_year= request.POST.get('study_year',None)
        Work = request.POST.get('work', None)
        Volunteer =request.POST.get('volunteer', None)
        Detail_work=request.POST.get('detail_work', None)
        Detail_vol = request.POST.get('detailvol', None)
        context = {}
        #context['userid'] = Uid
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            userPro=UserProfile.objects.get(StudentId=user)
            return render(request,'portfolio_subpages/profile.html')

        except UserProfile.DoesNotExist:
            user = Student.objects.get(studentId=request.session['userName'])
            user.YearOfStudy=Study_year
            user.save(update_fields=['YearOfStudy'])
            progress2=ProgressionBar.objects.get(StudentId=user)
            progress2.CurrentProgress=1
            progress2.save(update_fields=['CurrentProgress'])
            if Volunteer==None:
                Volunteer="no"
            test2 = UserProfile(StudentId=user, Work_exp=Work,FirstProgram=program,SecondProgram=program2, FirstMajor=major,SecondMajor=major2,Volunteer_exp=Volunteer,Detail_work=Detail_work,Detail_volunteer=Detail_vol)
            test2.save()

            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'portfolio.html')
            #return render(request, 'login.html')
    else:
        return render(request, 'current_profile.html')
