"""This is a custom Management command to add dummy users to the MyUser model
"""
from activity.models import MyUser
from django.core.management.base import BaseCommand, CommandError

from random import choice
import pytz


class Command(BaseCommand):
    """Command class that defines the Management Command

    Attributes:
        help: string containing a description of the management command
    """
    help = 'Adds a user to the MyUser model'

    def add_arguments(self, parser):
        """This method defines the arguments to be passed to the command

        Arguments:
            parser: an instance of class argparse.ArgumentParser
        """
        parser.add_argument(
            'user_id', nargs=1, help='user_id of the user to be added'
        )
        parser.add_argument('first_name', nargs=1, help='First name of the user')
        parser.add_argument('last_name', nargs=1, help='Last name of the user')
        parser.add_argument('password', nargs=1, help='Password of the user')

    def handle(self, *args, **options):
        """This logic contained in this method is what is run when the command
        is invoked

        """
        user_id = options['user_id'][0]
        first_name = options['first_name'][0]
        last_name = options['last_name'][0]
        password = options['password'][0]

        user = MyUser.objects.filter(user_id=user_id).first()
        if user:
            raise ValueError('user_id already exists')

        tz = choice(tuple(pytz.all_timezones_set))

        user = MyUser.objects.create_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            tz=tz,
            password=password
        )
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f'Added user_id: {user_id} to the MyUser model')
        )
