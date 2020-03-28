from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, user_id, first_name, last_name, password=None):
        if not user_id:
            raise ValueError('Users must have a user_id')

        user = self.model(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    user_id = models.CharField(max_length=20, unique=True, null=False, primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()


class ActivityPeriod(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
