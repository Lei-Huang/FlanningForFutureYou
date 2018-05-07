from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from django.core.exceptions import *
from django.views import View
from PFFU.form import *
from django.core.mail import send_mail
from datetime import *

# use session to keep user loginin, distinguished by username
def index(request):
    context = {}
    if request.method == 'GET':
        try:
            context['userName'] = request.session['userName']
            return render(request, 'index.html',context)
        except:
            return render(request, 'index.html')

    else:
        return render(request, 'index.html')

# def portfolio(request):
#         return render(request, 'portfolio.html')



class ForgetPwdView(View):
      def get(self, request):
          forget_form = ForgetPwdForm()
          return render(request, "forget_pwd.html", {"forget_form": forget_form})

      def post(self, request):
          forget_form = ForgetPwdForm(request.POST)
          if forget_form.is_valid():
              email = request.POST.get("email", "")
              send_mail("testing", "Did this work?", "no-reply@abc.net", ["email where you want to send ", ],
                        fail_silently=False)
              return render(request, "send_success.html")
          else:
              return render(request, "forget_pwd.html", {"forget_form": forget_form})


class ResetView(View):
          def get(self, request, active_code):
              all_records = EmailVerifyRecord.objects.filter(code=active_code)
              if all_records:
                  for record in all_records:
                      email = record.email
                      return render(request, "password_reset.html", {"email": email})
              else:
                  return render(request, "active_fail.html")
              return render(request, "login.html")


class ModifyPwdView(View):
      def post(self, request):
          modify_form = ModifyPwdForm(request.POST)
          if modify_form.is_valid():
              pwd1 = request.POST.get("password1", "")
              pwd2 = request.POST.get("password2", "")
              email = request.POST.get("email", "")
              if pwd1 != pwd2:
                  return render(request, "password_reset.html", {"email": email, "msg": u"password do not match"})
              user = UserProfile.objects.get(email=email)
              user.password = make_password(pwd1)
              user.save()
              return render(request, "login.html")
          else:
              email = request.POST.get("email", "")
              return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


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


def contact(request):
    return render(request, 'contact.html')


def workshops(request):

    context1 = {}

    if request.method == 'GET':

        try:
            user = Login.objects.get(StudentId=request.session.get('userName', None))
            user2 = Student.objects.get(studentId=request.session['userName'])
            progression = ProgressionBar.objects.get(StudentId=user2)
            if progression.CurrentProgress == 4:
                progression.CurrentProgress = 5
                progression.save(update_fields=['CurrentProgress'])
            context1['progressInt'] = int(progression.CurrentProgress)-1
            return render(request, 'portfolio_subpages/workshops.html', context1)

        except Login.DoesNotExist:

            return render(request, 'Needlogin.html')
    else:

        return render(request, 'login.html')

    #return render(request, 'portfolio_subpages/workshops.html')


def understanding_yourself(request):

    context1 = {}

    if request.method == 'GET':

        try:
            user = Login.objects.get(StudentId=request.session.get('userName', None))
            user2 = Student.objects.get(studentId=request.session['userName'])
            progression = ProgressionBar.objects.get(StudentId=user2)
            if progression.CurrentProgress == 1:
                progression.CurrentProgress = 2
                progression.save(update_fields=['CurrentProgress'])
            context1['progressInt'] = int(progression.CurrentProgress)-1

            return render(request, 'portfolio_subpages/understanding_yourself.html', context1)

        except Login.DoesNotExist:

            return render(request, 'Needlogin.html')
    else:

        return render(request, 'login.html')

    #return render(request, 'portfolio_subpages/understanding_yourself.html')


def employability_skill(request):
    return render(request, 'portfolio_subpages/employability_skill.html')

def future_skill(request):
    return render(request, 'portfolio_subpages/future_skill.html')

def re_em_info(request):
    return render(request, 'portfolio_subpages/re_em_info.html')

def uy_yes(request):
    return render(request, 'portfolio_subpages/uy_yes.html')


def uy_choice1(request):
    return render(request, 'portfolio_subpages/uy_choice1.html')

def uy_choice2(request):
    return render(request, 'portfolio_subpages/uy_choice2.html')


def research_employer(request):

    context1 = {}

    if request.method == 'GET':

        try:
            user = Login.objects.get(StudentId=request.session.get('userName', None))
            user2 = Student.objects.get(studentId=request.session['userName'])
            progression = ProgressionBar.objects.get(StudentId=user2)
            if progression.CurrentProgress == 3:
                progression.CurrentProgress = 4
                progression.save(update_fields=['CurrentProgress'])
            context1['progressInt'] = int(progression.CurrentProgress)-1
            return render(request, 'portfolio_subpages/research_employer.html', context1)

        except Login.DoesNotExist:
            return render(request, 'Needlogin.html')
    else:

        return render(request, 'login.html')

    #return render(request, 'portfolio_subpages/research_employer.html')


def interview_skill(request):

    context1 = {}

    if request.method == 'GET':

        try:
            user = Login.objects.get(StudentId=request.session.get('userName', None))
            user2 = Student.objects.get(studentId=request.session['userName'])
            progression = ProgressionBar.objects.get(StudentId=user2)
            context1['progressInt'] = int(progression.CurrentProgress)

            return render(request, 'portfolio_subpages/interview_skill.html', context1)

        except Login.DoesNotExist:

            return render(request, 'Needlogin.html')
    else:

        return render(request, 'login.html')

    #return render(request, 'portfolio_subpages/interview_skill.html')


def career_goaldone(request):
    return render(request, 'portfolio_subpages/career_goaldone.html')


def log(request):
    return render(request, 'test.html')


def career_goal(request):
    if request.method == 'GET':
        context = {}
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            userGoal = CareerGoal.objects.get(StudentId=user)
            context['cg_sector1'] = userGoal.Sector
            context['cg_goal1'] = userGoal.FirstRole
            context['cg_goal2']=userGoal.SecondRole
            context['cg_goal3']=userGoal.ThirdRole
            context['cg_q1'] = userGoal.FirstPlanSix
            context['cg_q2'] =  userGoal.FirstPlanTwelve
            context['cg_q3'] = userGoal.FirstPlanEighteen
            context['cg_q4'] = userGoal.SecondPlan
            context['cg_q5'] = userGoal.ThirdPlan
            context['feed_q1'] = userGoal.FirstPlanSixFeedback
            context['feed_q2'] = userGoal.FirstPlanTwelveFeedback
            context['feed_q3'] = userGoal.FirstPlanEighteenFeedback
            context['feed_q4'] = userGoal.SecondPlanFeedback
            context['feed_q5'] = userGoal.ThirdPlanFeedback

                    # do something with user
                    #html = ("<H1>User already exsit!</H1> ")
            return render(request,'portfolio_subpages/career_goaldone.html',context)
        except CareerGoal.DoesNotExist:
            return render(request,'portfolio_subpages/career_goal.html')
    if request.method == 'POST':
        sector = request.POST.get('cg_industry',None)
        firstRole = request.POST.get('firstgoal', None)
        secondRole = request.POST.get('secondgoal', None)
        thirdRole = request.POST.get('thirdgoal', None)
        FirstPlanSix= request.POST.get('cg_q1',None)
        FirstPlanTwelve = request.POST.get('cg_q2', None)
        FirstPlanEighteen =request.POST.get('cg_q3', None)
        SecondPlan = request.POST.get('cg_q4', None)
        ThirdPlan = request.POST.get('cg_q5', None)
        check_box_list2 = request.POST.getlist('cg_industry', None)
        l = ""
        for i in range(len(check_box_list2)):
            l = l + check_box_list2[i] + " "
        context = {}
        #context['userid'] = Uid
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            userPro=CareerGoal.objects.get(StudentId=user)
            return render(request,'portfolio_subpages/career_goal.html')

        except CareerGoal.DoesNotExist:
            user = Student.objects.get(studentId=request.session['userName'])
            #user.YearOfStudy=Study_year
            #user.save(update_fields=['YearOfStudy'])
            progress2=ProgressionBar.objects.get(StudentId=user)
            progress2.CurrentProgress=3
            progress2.save(update_fields=['CurrentProgress'])
            #if Volunteer==None:
             #   Volunteer="no"
            test2 = CareerGoal(StudentId=user,Sector=l,FirstRole=firstRole, SecondRole=secondRole,ThirdRole=thirdRole,FirstPlanSix=FirstPlanSix,FirstPlanTwelve=FirstPlanTwelve,FirstPlanEighteen=FirstPlanEighteen,SecondPlan=SecondPlan,ThirdPlan=ThirdPlan,pub_date=datetime.now())
            test2.save()
            context['progressInt']=progress2.CurrentProgress
            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'portfolio.html',context)
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
            user = Login.objects.get(StudentId = userName)
            #do something with user
            #html = (userName,"<H1>Success!</H1>")
            #context['userName'] = userName
            request.session['userName'] = userName
            # user logging in expiry time by seconds 
            request.session.set_expiry(3600)
            context1['userName'] = request.session['userName']
            if user.password==password:
            #request.session.clear()
                return render(request,'index.html',context1)
            else:
                return render(request, 'password_wrong.html')
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
            return render(request,'logout.html',context2)
            #return HttpResponse(html)
    else:
        request.session.clear()
        return render(request,'logout.html',context2)

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
            context['program'] = userProfile.FirstProgram
            context['major'] = userProfile.FirstMajor
            context['degree'] = user.Degree
            context['exp'] =  userProfile.Work_exp
            context['skill']=userProfile.Detail_work
            context['detail_vol'] = userProfile.Detail_volunteer
            context['start_date'] = userProfile.WorkStartDate
            context['end_date'] = userProfile.WorkEndDate
            context['study_year'] = user.YearOfStudy
            context['program2'] = userProfile.SecondProgram
            context['major2'] = userProfile.SecondMajor

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
        #Work = request.POST.get('work', None)
        Detail_work=request.POST.get('detail_work', None)
        Detail_vol = request.POST.get('detail_vol', None)
        start = request.POST.get('start_date', None)
        end = request.POST.get('end_date', None)
        check_box_list = request.POST.getlist('work',None)
        k = ""
        for i in range(len(check_box_list)):
            k=k+check_box_list[i]+" "
        context = {}
        #context['userid'] = Uid
        try:
            user = Student.objects.get(studentId=request.session['userName'])
            userProfile = UserProfile.objects.get(StudentId=user)
            context['Uid'] = user.studentId
            context['Lastname'] = user.LastName
            context['Firstname'] = user.FirstName
            context['Dis'] = user.Discipline
            context['program'] = userProfile.FirstProgram
            context['major'] = userProfile.FirstMajor
            context['degree'] = user.Degree
            context['exp'] = userProfile.Work_exp
            context['skill'] = userProfile.Detail_work
            context['detail_vol'] = userProfile.Detail_volunteer
            context['start_date'] = userProfile.WorkStartDate
            context['end_date'] = userProfile.WorkEndDate
            context['study_year'] = user.YearOfStudy
            context['program2'] = userProfile.SecondProgram
            context['major2'] = userProfile.SecondMajor
            user = Student.objects.get(studentId=request.session['userName'])
            userPro=UserProfile.objects.get(StudentId=user)
            userPro.FirstProgram=program
            userPro.SecondProgram = program2
            userPro.FirstMajor = major
            userPro.SecondMajor = major2
            user.YearOfStudy = Study_year
            userPro.Work_exp=Detail_work
            userPro.Detail_volunteer=Detail_vol

            userPro.save(update_fields=['FirstProgram'])
            userPro.save(update_fields=['SecondProgram'])
            userPro.save(update_fields=['FirstMajor'])
            userPro.save(update_fields=['SecondMajor'])
            user.save(update_fields=['YearOfStudy'])
            userPro.save(update_fields=['Work_exp'])
            userPro.save(update_fields=['Detail_volunteer'])
            return render(request,'portfolio_subpages/profile.html',context)

        except UserProfile.DoesNotExist:
            user = Student.objects.get(studentId=request.session['userName'])
            user.YearOfStudy=Study_year
            user.save(update_fields=['YearOfStudy'])
            progress2=ProgressionBar.objects.get(StudentId=user)
            progress2.CurrentProgress=1
            progress2.save(update_fields=['CurrentProgress'])
            if Detail_vol==None:
                Detail_vol="no"
            test2 = UserProfile(StudentId=user, Work_exp=k,FirstProgram=program,SecondProgram=program2,WorkStartDate=start,WorkEndDate=end, FirstMajor=major,SecondMajor=major2,Volunteer_exp="no",Detail_work=Detail_work,Detail_volunteer=Detail_vol)
            test2.save()

            # do something with user
            #html = ("<H1>User already exsit!</H1> ")
            return render(request, 'portfolio.html')
            #return render(request, 'login.html')
    else:
        return render(request, 'current_profile.html')
