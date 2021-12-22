"""fitnesssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from training.views import home, new_training, about, enlist, GroupSchedule
from abonement.views import index
from examination.views import Examination_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('abonement', index),
    path('groups', GroupSchedule.as_view(), name='group_schedule'),
    path('Examination', Examination_page.as_view(), name='examination'),
    path('appointment', new_training, name='new_training'),
    path('about', about, name='about'),
    path('groups/<int:group_id>/', enlist, name='join_group')
]
