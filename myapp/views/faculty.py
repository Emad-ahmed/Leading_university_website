from django.shortcuts import render
from django.views import View
from myapp.models import Faculty


def bba(request):
    bba_sir = Faculty.objects.filter(course_name="BBA")
    return render(request, 'bba.html', {'bba_sir': bba_sir})


def cse(request):
    cse_sir = Faculty.objects.filter(course_name="CSE")
    return render(request, 'cse.html', {'cse_sir': cse_sir})


def eng(request):
    eng_sir = Faculty.objects.filter(course_name="ENG")
    return render(request, 'eng.html', {'eng_sir': eng_sir})
