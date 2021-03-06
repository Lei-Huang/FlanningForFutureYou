from django.db import models
from datetime import datetime,timedelta
from django.utils import *


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    studentId = models.CharField(max_length=100, default='', primary_key = True)
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    LastName = models.CharField(max_length=100, null=True, blank=True)
    Degree= models.CharField(max_length=500, null=True, blank=True)
    Discipline = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    residentStatus = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    graduation_year = models.CharField(max_length=30, null=True, blank=True)
    YearOfStudy =models.CharField(max_length=100, null=True, blank=True)
    #owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    comments = models.TextField()
    def __str__(self):
        return self.studentId
    class Meta:
        ordering = ('created',)


class Login(models.Model):
    StudentId = models.CharField(max_length=100, blank=True, default='')
    StaffId = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=60)


class Staff(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    StaffId = models.CharField(max_length=100, default='', primary_key = True)
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Email = models.EmailField(blank=True, verbose_name='e-mail')
    PhoneNumber= models.CharField(max_length=30)
    ModifyDate = models.DateTimeField()
    StudentId =models.ForeignKey(Student,on_delete=models.CASCADE)
    Description = models.TextField()
    UserProfileYear =models.CharField(max_length=20)
    #owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    #highlighted = models.TextField()



class UserProfile(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    FirstProgram = models.CharField(max_length=500, null=True, blank=True)
    SecondProgram = models.CharField(max_length=500, null=True, blank=True)
    FirstMajor = models.CharField(max_length=500, null=True, blank=True)
    SecondMajor = models.CharField(max_length=500, null=True, blank=True)
    # ProfileType = models.CharField(max_length=20)
    # NetworkTree = models.CharField(max_length=30)
    # SkillTree = models.CharField(max_length=30)
    # ExperienceTree = models.CharField(max_length=30)
    # PreparationTree = models.CharField(max_length=30)
    WorkStartDate = models.CharField(max_length=50, null=True, blank=True)
    Work_exp = models.CharField(max_length=100, null=True, blank=True)
    WorkEndDate = models.CharField(max_length=50, null=True, blank=True)
    Volunteer_exp = models.CharField(max_length=100, null=True, blank=True)
    Detail_work = models.TextField()
    Detail_volunteer = models.TextField()
    # Network = models.TextField()
    # Skill = models.TextField()
    # Experience = models.TextField()
    # Preparation = models.TextField()
    # Notes = models.TextField()


class ProgressionBar(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    CurrentProgress = models.IntegerField(default="")


class CareerVoyage(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)


class CareerGoal(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)
    Sector = models.CharField(max_length=200)
    FirstRole = models.CharField(max_length=100)
    SecondRole = models.CharField(max_length=100)
    ThirdRole = models.CharField(max_length=100)
    FirstPlanSix = models.TextField(verbose_name="Six month plan")
    FirstPlanSixFeedback=models.TextField(default="Waiting for feedback")
    FirstPlanTwelve = models.TextField(verbose_name="Twelve month plan")
    FirstPlanTwelveFeedback = models.TextField(default="Waiting for feedback")
    FirstPlanEighteen = models.TextField(verbose_name="Eighteen month plan")
    FirstPlanEighteenFeedback = models.TextField(default="Waiting for feedback")
    SecondPlan = models.TextField(verbose_name="Gain ability")
    SecondPlanFeedback = models.TextField(default="Waiting for feedback")
    ThirdPlan = models.TextField(verbose_name="Expend network")
    ThirdPlanFeedback = models.TextField(default="Waiting for feedback")
    pub_date = models.DateTimeField('date submit')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)
        pass

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class CareerValue(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)
    FormInfo = models.CharField(max_length=200)


class ResearchEmployer(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)


class ResearchJob(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)


class InterviewSkills(models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)


class EmailVerify(models.Model):
     StudentId = models.ForeignKey(Student,on_delete=models.CASCADE)
     code = models.CharField(max_length=200)
     email = models.CharField(max_length=200)