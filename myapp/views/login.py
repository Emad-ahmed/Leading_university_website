from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})

    def post(self, request):
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Login')
                return HttpResponseRedirect('/')
        return render(request, 'login.html', {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('user_login')
