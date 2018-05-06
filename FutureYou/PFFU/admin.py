from django.contrib import admin
from .models import Student
from .models import UserProfile
from .models import Staff
from .models import ProgressionBar

admin.site.register(UserProfile)
admin.site.register(Staff)
admin.site.register(ProgressionBar)
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    # ...
    list_display = ('studentId', 'Discipline', 'Degree')
    list_filter = ['created']
    search_fields = ['studentId']

admin.site.register(Student,StudentAdmin)