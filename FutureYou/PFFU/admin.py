from django.contrib import admin
from .models import Student
from .models import UserProfile
from .models import Staff
from .models import ProgressionBar

admin.site.register(Staff)
# Register your models here.


class ChoiceInline(admin.StackedInline):
    model = UserProfile
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ('studentId','FirstName','LastName','Degree','Discipline')}),
        ('More Information',{'classes': ('collapse',),
            'fields':('graduation_year','YearOfStudy','comments') })
    ]
    inlines = [ChoiceInline]
    list_display = ('studentId', 'Discipline', 'Degree')
    list_filter = ['created']
    search_fields = ['studentId']


class UserprofileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ('StudentId','FirstProgram','SecondProgram','FirstMajor','SecondMajor','Detail_work','Detail_volunteer')})
    ]
    list_display = ('StudentId', 'FirstProgram', 'FirstMajor')
    list_filter = ['StudentId']
    search_fields = ['StudentId']

class ProgressionBarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ('StudentId','CurrentProgress')})
    ]
    list_display = ('StudentId', 'CurrentProgress')
    search_fields = ['StudentId']

admin.site.register(Student,StudentAdmin)
admin.site.register(UserProfile,UserprofileAdmin)
admin.site.register(ProgressionBar,ProgressionBarAdmin)