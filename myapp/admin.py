from django.contrib import admin
from myapp.models import Notice, News, Faculty, Students, StudentResult, Courses, SessionYearModel, Subjects
# Register your models here.


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name']


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(SessionYearModel)
class SessionYearModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_start_year', 'session_end_year']


@admin.register(Subjects)
class SubjectsModelAdmin(admin.ModelAdmin):
    list_display = ['id']
