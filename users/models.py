from django.db import models


class Heartrate(models.Model):
    user_heartrate = models.FloatField()