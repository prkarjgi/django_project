from django.urls import path
from .views import activityperiod, run_management_commands


urlpatterns = [
    path('api/activity', activityperiod, name='activity_period'),
    path('api/command', run_management_commands, name='run_management_commands')
]
