from django.urls import path
from . import views

app_name="VoterProfileApp"

urlpatterns = [
    path('login-page/',views.login_page,name="login"),
    path('see/',views.voter_profile,name="voter-profile"),
    path('voter-login-success/',views.voter_login_success,name="voter-login-success"),
    path('voter-logout/', views.voter_logout, name="voter-logout"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('changepassword-submit/',views.changepassword_submit,name="changepassword-submit"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('check-forgot-password/',views.check_forgot_password,name="check-forgot-password"),
    ]
