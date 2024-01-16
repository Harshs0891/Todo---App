from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=300)
    start_time = models.TimeField()
    end_time = models.TimeField()