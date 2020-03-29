from django.urls import path
from .views import activityperiod


urlpatterns = [
    path('activity', activityperiod, name='activity_period')
]
