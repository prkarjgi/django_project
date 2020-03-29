## Django Application

### Description
This is a Django application used to create and retrieve Activity Period data. It is hosted on heroku at [here](https://prkarjgi-django.herokuapp.com).


### Features
#### Models
1. MyUser: extends the base User model provided by Django
    Columns:
    * **user_id**: primary key, unique hex string
    * **first_name**: first name of the user
    * **last_name**: last name of the user
    * **tz**: timezone of the user, kept fixed
    * **password**: password of the user
    * **last_login**: last login, null

2. ActivityPeriod: stores the start and end times of a user
    Columns:
    * **id**: primary key, autoincremented key
    * **user**: foreign key referencing a user in the MyUser model
    * **start_time**: timezone aware start time of activity of a user in UTC
    * **end_time**: timezone aware end time of activity of a user in UTC


#### Custom Management
1. **add_user**: Adds a randomised user with randomized name and timezone to the MyUser model
    usage: python manage.py add_user
2. **add_activity**: Adds dummy activity data for all users in MyUser model to the ActivityPeriod model
    usage: python manage.py add_activity

These commands can be triggered using an API endpoint shown below.


#### API endpoint
This app has API endpoints exposed as shown:
HTTP Method | URI | Action
--- | --- | ---
GET | https://prkarjgi-django.herokuapp.com/api/activity | Retrieves data from MyUser and ActivityPeriod models according to specifications
GET | https://prkarjgi-django.herokuapp.com/api/command | Runs Management Commands to populate the Models with dummy data

