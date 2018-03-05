from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name



class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    studentId = models.CharField(max_length=100, blank=True, default='')
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Degree= models.CharField(max_length=30)
    Discipline = models.CharField(max_length=30)
    description = models.TextField()
    residentStatus = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    graduation_year = models.CharField(max_length=30)
    YearOfStudy =models.CharField(max_length=10)
    owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)


class Login(models.Model):
    StudentId = models.CharField(max_length=100, blank=True, default='')
    StaffId = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=60)


class Staff(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    StaffId = models.CharField(max_length=100, blank=True, default='')
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Email = models.EmailField(blank=True, verbose_name='e-mail')
    PhoneNumber= models.CharField(max_length=30)
    ModifyDate = models.DateTimeField()
    StudentId =models.ForeignKey(Student)
    Description = models.TextField()
    UserProfileYear =models.CharField(max_length=20)
    #owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    #highlighted = models.TextField()

class MainEvent(models.Model):
    EventId = models.CharField(max_length=20)
    EvenType = models.CharField(max_length=20)
    EventDate= models.DateTimeField()
    EventContent = models.TextField()


class BadgeInfo(models.Model):
    BageInfoId = models.CharField(max_length=20)
    BageName = models.CharField(max_length=40)
    Deprecation = models.TextField()
    Relatiom = models.CharField(max_length=50)
    Imageurl = models.URLField()


class UserProfile(models.Model):
    StudentId = models.ForeignKey(Student)
    ProfileYear = models.CharField(max_length=20)
    ProfileType = models.CharField(max_length=20)
    NetworkTree = models.CharField(max_length=30)
    SkillTree = models.CharField(max_length=30)
    ExperienceTree = models.CharField(max_length=30)
    PreparationTree = models.CharField(max_length=30)
    Network = models.TextField()
    Skill = models.TextField()
    Experience = models.TextField()
    Preparation = models.TextField()
    Notes = models.TextField()


class Badge(models.Model):
    BadgeId = models.CharField(max_length=20)
    BadgeStatus = models.CharField(max_length=30)
    BadgeInfo = models.ForeignKey(BadgeInfo)


class Incentive(models.Model):
    IncentiveId = models.CharField(max_length=20)
    IncentiveType = models.CharField(max_length=30)
    Description = models.TextField()


class Points(models.Model):
    PointsId = models.CharField(max_length=20)
    CurrentPoints = models.CharField(max_length=20)


class UserEvent(models.Model):
    StudentId = models.ForeignKey(Student)
    UserEventId = models.CharField(max_length=20)
    UserEventType = models.CharField(max_length=20)
    UserEventDate = models.DateTimeField()
    UserEventContent = models.TextField()
