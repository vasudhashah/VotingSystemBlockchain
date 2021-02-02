from django.urls import path
from . import views
app_name="CandidateApp"

urlpatterns = [
    path('ec-login/',views.ec_login,name='ec-login'),
    path('ec-login-success/',views.ec_login_success,name='ec-login-success'),
    path('ec-home/',views.ec_home,name='ec-home'),
    path('ec-logout/', views.ec_logout, name='ec-officer-logout'),
    path('candidate-register-home', views.candidate_register_home, name='candidate-register-home'),
    path('candidate-register-success', views.candidate_register_success, name='candidate-register-success')
]
