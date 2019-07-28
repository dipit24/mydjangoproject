"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views
from login_myapp import views as lv
from sessionmanagement import views as sv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello, name='Hello'),
    path('validation/',views.validation,name='Validation'),
    path('index/',views.index, name='Index'),
    path('',views.index, name='Index'),
    path('delete/<int:id>',views.del_emp,name='del_emp'),
    path('addcompany/',views.add_company, name='add_company'),
    path('addlanguage/',views.add_language, name='add_language'),
    path('addemployee/',views.add_employee, name='add_employee'),
    path('msg/',views.msg,name='msg'),
    path('login_myapp/',include('login_myapp.urls')),
    path('CBV/',include('ClassBasedViews.urls')),
    path('login_index/',lv.index,name='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('session/',sv.session,name='session'),
]