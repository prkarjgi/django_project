"""
"""
from activity.models import MyUser
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """
    """
    help = 'Adds a user to the MyUser model'

    def add_arguments(self, parser):
        parser.add_argument(
            'user_id', nargs=1, help='user_id of the user to be added'
        )
        parser.add_argument('first_name', nargs=1, help='First name of the user')
        parser.add_argument('last_name', nargs=1, help='Last name of the user')
        parser.add_argument('password', nargs=1, help='Password of the user')

    def handle(self, *args, **options):
        user_id = options['user_id'][0]
        first_name = options['first_name'][0]
        last_name = options['last_name'][0]
        password = options['password'][0]

        user = MyUser.objects.filter(user_id=user_id).first()
        if user:
            raise ValueError('user_id already exists')

        user = MyUser.objects.create_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f'Added user_id: {user_id} to the MyUser model')
        )
