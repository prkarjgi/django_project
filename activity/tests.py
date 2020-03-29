from django.test import TestCase
from activity.models import MyUser, ActivityPeriod


class UserTestCase(TestCase):
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
            tz='Asia/Kolkata',
            password='production'
        )
        user1.save()
        user2.save()

    def test_create_user(self):
        users = MyUser.objects.count()
        self.assertEqual(users, 2)
