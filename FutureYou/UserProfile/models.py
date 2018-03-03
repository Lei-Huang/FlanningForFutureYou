from django.db import models
# from django.contrib.auth.models import User
import uuid
# Create your models here.

STUDY_STATUS = (
    ('U','Undergraduate'),
    ('P','Postgraduate'),
)

class UserGroup(models.Model):
    name = models.CharField(max_length=50)

    # class Meta:
    #     verbose_name = "UserGroup"
    #     verbose_name_plural = "UserGroups"

    def __str__(self):
        return '%s' % self.name

class BasicProfile(models.Model):
    profile_id = models.CharField(editable=False,default=str(uuid.uuid4().hex), primary_key=True, max_length=64)
    first_name = models.CharField(default='',null=True,max_length=50)
    last_name = models.CharField(default='',null=True,max_length=50)
    user_group = models.ForeignKey(UserGroup)
    study_status = models.CharField("Study Status", choices=STUDY_STATUS, default='U',null=False, blank=True, max_length=32)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)