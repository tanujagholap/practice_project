from django.urls import path
from .views import *


urlpatterns = [
    path('', create_view, name='create_url'),
    path('retrieve/', retrieve_view, name='retrieve_url'),
    path('update/<int:pk>/', update_view, name='update_url'),
    path('create/<int:pk>/', delete_view, name='delete_url'),

]