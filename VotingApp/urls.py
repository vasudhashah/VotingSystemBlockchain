from django.urls import path
from . import views

app_name="VotingApp"

urlpatterns = [
    path('login/',views.loginn,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.officer_logout,name='logout'),
    path('officer-login-success/',views.officer_login_success,name='officer-login-success'),
    path('display-candidates/', views.display_candidates, name='display-candidates')
]
