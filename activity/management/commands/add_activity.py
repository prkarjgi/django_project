"""This is a custom Management Command to add dummy activity data
to the ActivityPeriod model
"""
from datetime import timedelta, datetime

from activity.models import MyUser, ActivityPeriod
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

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

        The command accepts a list of user_ids as an argument. It will iterate
        through the list and check if the given user_id exists in the MyUser
        model. If the user_id is not found, a CommandError is raised.

        While adding activity for a user, 2 rows are added to the ActivityPeriod
        model. First an initial start time is taken in UTC, an arbitrary value
        of 2 hours is added as the end time for the first row.
        For the second row, an offset of 30 days is added to the initial
        time. The end time is offset by 2 hours and 30 days from the initial
        time.
        """
        for user_id in options['user_ids']:
            user = MyUser.objects.filter(user_id=user_id).first()
            if not user:
                raise CommandError(f'user_id: {user_id} does not exist.')

            start = timezone.now()

            act1 = ActivityPeriod(
                myuser=user,
                start_time=start,
                end_time=start + timedelta(hours=2)
            )
            act2 = ActivityPeriod(
                myuser=user,
                start_time=start + timedelta(days=30),
                end_time=start + timedelta(hours=2, days=30)
            )
            act1.save()
            act2.save()

            self.stdout.write(
                self.style.SUCCESS(f'SUCCESS: Activity added for user_id: {user_id}')
            )
