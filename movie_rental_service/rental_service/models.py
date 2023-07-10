from django.db import models

class Movie(models.Model):
    Title = models.CharField(max_length=100)
    Release_date=models.DateField()
    Genre=models.CharField(max_length=100)
    Duration_minutes=models.IntegerField()
    Rating=models.FloatField()
