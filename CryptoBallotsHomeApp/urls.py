from django.urls import path
from . import views
app_name="CryptoBallotsHomeApp"

urlpatterns = [
    path('',views.home,name='home'),
]
