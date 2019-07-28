from django.urls import path,include
from login_myapp import views
from django.shortcuts import render

urlpatterns=[
    path('',views.myapp_login_index,name='myapp_login_index'),
    path('signup_user',views.signup_user,name='signup_user'),
    path('registration_success/',lambda request:render(request,'login_myapp/registration_success.html'),name='registration_success'),
    path('login_profile/',views.profile,name='login_profile')
    ]
    