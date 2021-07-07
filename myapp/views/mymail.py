from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
import requests


class EmailView(View):
    def get(self, request):
        response = requests.get(
            'https://api.covidtracking.com/v2/us/daily.json').json()
        return render(request, 'mymail.html', {'response': response})

    def post(self, request):
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        to_email = request.POST.get('to_email')
        from_email = 'amadahmed1234678@gmail.com'
        to_email = [to_email]
        send_mail(subject, message, from_email, to_email)
        messages.success(request, "Successfully Send Email")
        return render(request, 'mymail.html')
