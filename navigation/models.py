from django.db import models

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="navigation_records")
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

