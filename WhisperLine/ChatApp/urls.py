from django.urls import path
from . import views

urlpatterns = [
    # path('', views., name='base'), 
    path('register/',views.register,name='register'),
    path("groups/", views.group_chat_list, name="group_chat_list"),
    path("groups/<int:group_id>/", views.group_chat_room, name="group_chat_room"),
    path("private/<int:receiver_id>/", views.private_chat, name="private_chat"),
]
