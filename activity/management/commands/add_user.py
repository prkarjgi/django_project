"""This is a custom Management command to add dummy users to the MyUser model
"""
from activity.models import MyUser
from django.core.management.base import BaseCommand, CommandError

from random import choice
from typing import List
import pytz
import uuid


class Command(BaseCommand):
    """Command class that defines the Management Command

    Attributes:
        help: string containing a description of the management command
    """
    help = 'Adds a user to the MyUser model'

    def handle(self, *args, **options):
        """This logic contained in this method is what is run when the command
        is invoked

        The command randomly generates a user_id for the new user and checks
        that the new id is not in the MyUser model.
        A first name and last name are randomly chosen from the lists below
        and the timezone is selected at random from list of
        pytz.all_timezone_set. The same password is added for each dummy user.
        """

        users = MyUser.objects.all()
        user_ids = [user.user_id for user in users]
        if not user_ids:
            user_id = str(uuid.uuid4())
        else:
            user_id = generate_user_id(user_ids)

        first_name = choice(['Kawhi', 'Kevin', 'LeBron', 'Stephen', 'James'])
        last_name = choice(['Leonard', 'Durant', 'James', 'Curry', 'Harden'])
        tz = choice(tuple(pytz.all_timezones_set))
        password = 'testing'

        user = MyUser.objects.create_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            tz=tz,
            password=password
        )
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f'SUCCESS: Added user_id: {user_id} to the MyUser model')
        )


def generate_user_id(user_ids: List[str]) -> str:
    x = str(uuid.uuid4())
    while(1):
        if x in user_ids:
            x = str(uuid.uuid4())
        else:
            break
    return x
