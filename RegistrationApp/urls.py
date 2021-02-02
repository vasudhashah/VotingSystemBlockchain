from django.urls import path
from . import views

app_name="RegistrationApp"

urlpatterns = [
    path('register/',views.home,name="home"),
    path('user-register-success', views.user_register_success, name="user-register-success"),
    path('login/',views.login_window,name="login"),
    path('officer-login-success/', views.officer_login_success, name="officer-login-success"),
    path('officer-logout/', views.officer_logout, name="officer-logout"),
    path('ok-clicked/',views.ok,name="ok"),
    path('update-window/',views.update_window,name="update-window"),
    path('save-update-details/', views.save_update_details, name="save-update-details"),

    path('user_register_window/', views.user_register_window, name = 'user_register_window'),
	path('success/', views.success, name = 'success'),
]
