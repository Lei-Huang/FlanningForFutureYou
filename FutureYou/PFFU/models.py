from django.db import models



class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    studentId = models.CharField(max_length=100, default='', primary_key = True)
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Degree= models.CharField(max_length=30)
    Discipline = models.CharField(max_length=30)
    description = models.TextField()
    residentStatus = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    graduation_year = models.CharField(max_length=30)
    YearOfStudy =models.CharField(max_length=10)
    #owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    highlighted = models.TextField()

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
    # Todo check on_delete
    StudentId =models.ForeignKey(Student,on_delete=models.CASCADE)

    Description = models.TextField()
    UserProfileYear =models.CharField(max_length=20)
    #owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    #highlighted = models.TextField()



class UserProfile(models.Model):
    # Todo check on_delete
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    StudyYear = models.CharField(max_length=20)
    FirstProgram = models.CharField(max_length=100)
    SecondProgram = models.CharField(max_length=100)
    FirstMajor = models.CharField(max_length=100)
    SecondMajor = models.CharField(max_length=100)
    # ProfileType = models.CharField(max_length=20)
    # NetworkTree = models.CharField(max_length=30)
    # SkillTree = models.CharField(max_length=30)
    # ExperienceTree = models.CharField(max_length=30)
    # PreparationTree = models.CharField(max_length=30)
    WorkStartDate = models.CharField(max_length=50)
    Work_exp = models.CharField(max_length=30)
    WorkEndDate = models.CharField(max_length=50)
    Volunteer_exp = models.CharField(max_length=30)
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
    Sector = models.CharField(max_length=30)
    FirstRow = models.CharField(max_length=100)
    SecondRow = models.CharField(max_length=100)
    ThirdRow = models.CharField(max_length=100)
    FirstPlan = models.TextField()
    SecondPlan = models.TextField()
    ThirdPlan = models.TextField()


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


# class UserEvent(models.Model):
#     StudentId = models.ForeignKey(Student,on_delete=models.CASCADE)
#     UserEventId = models.CharField(max_length=20)
#     UserEventType = models.CharField(max_length=20)
#     UserEventDate = models.DateTimeField()
#     UserEventContent = models.TextField()
