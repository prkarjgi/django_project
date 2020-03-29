from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    """Custom Manager for custom User model that provides an extra method
    to add users to the MyUser model

    """
    def create_user(self, user_id, first_name, last_name, tz, password=None):
        """Method that is used to create a new user in the MyUser model

        Arguments:
            user_id: string that represents the unique user id
            first_name: string, first name of the user
            last_name: string, last name of the user
            tz: string, timezone assumed to be fixed for the user at a time
            password: string, password of the user
        """
        if not user_id:
            raise ValueError('Users must have a user_id')

        user = self.model(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            tz=tz
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """Custom User model that substitutes the built-in User model provided by
    Django

    Attributes:
        user_id: 20 character long field that acts as a primary key for each user
        first_name: character field representing the first name of the user,
            cannot be null
        last_name: character field representing the last name of the user,
            cannot be null
        tz: character field used to represent the timezone of the user
    """
    user_id = models.CharField(max_length=36, unique=True, null=False, primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    tz = models.CharField(max_length=30)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.user_id


class ActivityPeriod(models.Model):
    """Model used to store the start time and end time of a user's activity
    on the app

    Attributes:
        myuser: column that acts as Foreign key, establishes a many-to-one
            relationship with the MyUser model
        start_time: timezone aware datetime field that represents the start
            time of a user's activity on the app. Stores datetime in UTC.
        end_time: timezone aware datetime field that represents the end time
            of a user's activity on the app. Stores datetime in UTC.
    """
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.myuser.user_id
