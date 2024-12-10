from django.urls import path
from . import views

urlpatterns = [
    # path('', views., name='base'), 
    path('register/',views.register,name='register'),
]
