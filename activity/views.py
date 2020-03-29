"""View functions used by the API
"""
import json
import pytz
from io import StringIO

from django.shortcuts import render
from django.core.management import call_command
from django.http import HttpResponse, JsonResponse
from .models import MyUser, ActivityPeriod


def run_management_commands(request):
    out = StringIO()
    call_command('add_user', stdout=out)
    add_user_result = out.getvalue()

    call_command('add_activity', stdout=out)
    add_activity_result = out.getvalue()
    response = {
        'add_user result': add_user_result,
        'add_activity result': add_activity_result
    }
    return JsonResponse(response, json_dumps_params={'indent': 4})


def activityperiod(request):
    """This is the view function that handles the API request

    If the method of the request is GET, then the required data is returned.
    The MyUser model is queried to retrieve all the users. The QuerySet of the
    users is iterated over and the activity periods for that member are
    retrieved.

    The timezone for each user is assumed to be fixed and the start_time
    and end_time, which are timezone aware DateTimeFields in UTC, are
    converted into the local time with respect to the timezone of the user.
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
