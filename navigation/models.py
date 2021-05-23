from django.db import models

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="navigation_records")
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Improvement!!
    # Some databases already does something for datetime indexing but for improvement, 
    # it would help to index datetime as it would make searching by datetime faster.
    # As far as I know, some databases only does indexing by date which is more than 10x faster
    # than datetime since it doesn't count for time and miliseconds
    # Fore more information: https://stackoverflow.com/questions/17381875/how-to-improve-performance-for-datetime-filtering-in-sql-server
    class Meta:
        indexes = [
            models.Index(fields=['datetime'], name='datetime_idx'),
        ]