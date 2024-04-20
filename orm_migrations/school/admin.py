from django.contrib import admin

from .models import Student, Teacher

class StudentInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [StudentInline]
    exclude = ['teachers']
    list_filter = ['group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    list_filter = ['subject']
