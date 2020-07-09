from django.urls import path
from . import views

urlpatterns=[
    path("room",views.room,name="room"),
    path("",views.login,name="login"),
    path("register/",views.register,name="register"),
    path('logout',views.logout,name='logout'),
]