from django.contrib import admin
from faculty.models import *
# Register your models here.
class StudentInline(admin.TabularInline):
    model = Student
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'building','mission']
    search_fields = ['name']
    ordering = ['name']
    inlines = [StudentInline]

    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','salary']
    search_fields = ['name','email']
    ordering = ['name']
    filter_horizontal = ['department']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id','name', 'department']
    search_fields = ['name','student_id']
    ordering = ['name']
    list_filter = ['department']


