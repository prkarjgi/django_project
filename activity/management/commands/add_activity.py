"""This is a custom Management Command to add dummy activity data
to the ActivityPeriod model
"""
from datetime import datetime

from activity.models import MyUser, ActivityPeriod
from django.core.management.base import BaseCommand, CommandError

import pytz


class Command(BaseCommand):
    """Command class that defines the management command used

    The command can be called as: python manage.py add_activity args

    Attributes:
        help: string containing a description of the command
    """
    help = 'Adds dummy user activity to the ActivityPeriod model'

    def add_arguments(self, parser):
        """This method defines the arguments to be passed to the command

        Arguments:
            parser: an instance of class argparse.ArgumentParser
        """
        parser.add_argument(
            'user_ids',
            nargs='+',
            help='list of user_ids for which dummy activity data will be added'
        )

    def handle(self, *args, **options):
        """This logic contained in this method is what is run when the command
        is invoked

        """
        for user_id in options['user_ids']:
            try:
                user = MyUser.objects.filter(user_id=user_id).first()
            except MyUser.DoesNotExist:
                raise CommandError(f'user_id: {user_id} does not exist.')
