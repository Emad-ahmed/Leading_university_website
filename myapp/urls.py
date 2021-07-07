from myapp.views.faculty import eng
from django.urls import path
from myapp.views import HomeView, shownotice, shownews, LoginView, SignupView, user_logout, EmailView, bba, cse, eng, StudentView
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm, MySetPasswordForm, MyPasswordChangeForm

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('user_login', LoginView.as_view(), name="user_login"),
    path('student', StudentView.as_view(), name="student"),
    path('user_logout', user_logout, name="user_logout"),
    path('signup', SignupView.as_view(), name="signup"),
    path('shownotice/<int:id>', shownotice, name="shownotice"),
    path('shownews/<int:id>', shownews, name="shownews"),
    path('mymail', EmailView.as_view(), name="mymail"),
    path('bba', bba, name="bba"),
    path('cse', cse, name="cse"),
    path('eng', eng, name="eng"),

    # Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),


    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),


    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),



    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',
                                                                  form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='passwordchangedone.html'), name='passwordchangedone'),

]
