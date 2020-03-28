"""
"""
from datetime import datetime

from activity.models import MyUser, ActivityPeriod
from django.core.management.base import BaseCommand, CommandError

import pytz


class Command(BaseCommand):
    """
    """
    help = 'Adds dummy user activity to the ActivityPeriod model'

    def add_arguments(self, parser):
        parser.add_argument(
            'user_ids',
            nargs='+',
            help='list of user_ids for which dummy activity data will be added'
        )

    def handle(self, *args, **options):
        for user_id in options['user_ids']:
            try:
                user = MyUser.objects.filter(user_id=user_id).first()
            except MyUser.DoesNotExist:
                raise CommandError(f'user_id: {user_id} does not exist.')
