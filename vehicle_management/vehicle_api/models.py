from django.db import models

class Car(models.Model):
     vehicle_number = models.CharField(max_length=20)
     availability = models.BooleanField(default=True)
     manufacturer=models.CharField(max_length=20)

class Task(models.Model):
     car = models.ForeignKey(Car, on_delete=models.CASCADE)
     owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)



   
