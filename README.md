# AV-FMS

is a system that manages the autonomous vehicles in the fleet. God
The system stores the catalog of vehicles and their characteristics and allows registered users to make and track changes and manage
The DB

installation instructions:

1.Download the zip file

2.Enter the folder vehicle_management

3.Download the packages that rewritten in the requirements file.

4.run the server.


activity function:


api/user/create/ -create the user

api/user/token/  -post the email and password and get  a token for all the Authentication function.


api/car/  -get all the cars filtering is possible

api/car/create  -create car  for admin

api/task  -get all the task

api/task/create-task -create tesk for user.

api/task/release-task -release task for user

I chose DB SQLITE because I saw that it works easily with DJANGO.
To view the data you can use the website https://inloop.github.io/sqlite-viewer/
and drag the db.sqlite3 file there.





