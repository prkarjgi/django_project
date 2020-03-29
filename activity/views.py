import json
from django.shortcuts import render
from .models import MyUser, ActivityPeriod


def activityperiod(request):
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
            member['activity'] = []
            activity = ActivityPeriod.objects.filter(myuser=user)

        return json.dumps(resp)
