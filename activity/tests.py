from io import StringIO

from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError

from activity.models import MyUser, ActivityPeriod


class UserTestCase(TestCase):
    """Class used to test adding users to the MyUser model

    """
    def setUp(self):
        user1 = MyUser.objects.create_user(
            user_id='Q100',
            first_name='Test',
            last_name='Case',
            tz='America/Los_Angeles',
            password='testing'
        )
        user2 = MyUser.objects.create_user(
            user_id='Q101',
            first_name='Fake',
            last_name='Name',
            tz='America/Puerto_Rico',
            password='production'
        )
        user1.save()
        user2.save()

    def test_create_user(self):
        users = MyUser.objects.count()
        self.assertEqual(users, 2)


class AddUserTestCase(TestCase):
    """Class used to test the 'add_user' management command used to add a user
    to the MyUser model

    """
    def test_add_user(self):
        out = StringIO()
        call_command('add_user', stdout=out)
        self.assertIn('SUCCESS', out.getvalue())


class AddActivityTestCase(TestCase):
    """Class used to test the 'add_activity' management command to add dummy
    activity data to the ActivityPeriod model

    """
    def setUp(self):
        user1 = MyUser.objects.create_user(
            user_id='Q102',
            first_name='Test',
            last_name='Case',
            tz='Asia/Kolkata',
            password='testing'
        )
        user1.save()

    def test_add_activity(self):
        out = StringIO()
        call_command('add_activity', stdout=out)
        self.assertIn('SUCCESS', out.getvalue())
