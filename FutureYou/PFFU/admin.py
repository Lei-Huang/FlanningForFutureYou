from django.contrib import admin
from .models import Student
from .models import UserProfile
from .models import Staff
from .models import ProgressionBar
admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(Staff)
admin.site.register(ProgressionBar)

# Register your models here.
