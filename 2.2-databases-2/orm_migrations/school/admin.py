from django.contrib import admin

from .models import Student, Teacher, TeacherStudent

class StudentTeacherInline(admin.TabularInline):
    model = TeacherStudent
    extra = 3

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentTeacherInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']