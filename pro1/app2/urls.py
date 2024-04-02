from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('sign_up/', signup_view, name='signup_url'),


]