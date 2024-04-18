from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signup_view, name='signup_url'),
    path('otp/', otp_view, name='otp_url'),
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
]
