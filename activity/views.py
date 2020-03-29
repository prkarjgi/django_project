"""
"""
import json
import pytz

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MyUser, ActivityPeriod


def activityperiod(request):
    """
    """
    if request.method == 'GET':
        resp = {}
        resp['ok'] = True
        resp['members'] = []
        users = MyUser.objects.all()
        for user in users:
            member = {}
            member['id'] = user.user_id
            member['real_name'] = f'{user.first_name} {user.last_name}'
            member['tz'] = user.tz
            member['activity_periods'] = []
            activity = ActivityPeriod.objects.filter(myuser=user)
            for each in activity:
                period = {}
                period['start_time'] = convert_timezone(
                    dt=each.start_time,
                    tz=user.tz,
                    dt_format='%b %-d %Y  %-I:%M%p'
                )
                period['end_time'] = convert_timezone(
                    dt=each.end_time,
                    tz=user.tz,
                    dt_format='%b %-d %Y %-I:%M%p'
                )
                member['activity_periods'].append(period)
            resp['members'].append(member)
        return JsonResponse(resp, json_dumps_params={'indent': 4})


def convert_timezone(dt, tz, dt_format: str) -> str:
    """
    """
    converted_dt = dt.astimezone(pytz.timezone(tz)).strftime(dt_format)
    return converted_dt
