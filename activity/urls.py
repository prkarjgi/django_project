from django.urls import path
from . import views


urlpatterns = [
    path('api/activity', views.activityperiod, name='activity_period'),
    path('api/command', views.run_management_commands, name='run_management_commands'),
    path('', views.home, name='home')
]
