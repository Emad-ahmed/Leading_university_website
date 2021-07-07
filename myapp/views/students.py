from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import Students, StudentResult, student


class StudentView(View):
    def get(self, request):
        my_student = Students.objects.get(admin=request.user)
        myiid = my_student.student_id_no
        print(myiid)
        myresult = StudentResult.objects.filter(myid=myiid)
        print(myresult)

        return render(request, 'student_result.html', {'stu': my_student, 'myresult' : myresult})
