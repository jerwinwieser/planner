from django.db import models

import datetime


class Snippet(models.Model):
	name = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return self.name


class Person(models.Model):
	TIME_CHOICES = (
	    ("SHORT", "Short"),
	    ("LONG", "Long"),
	)
	current_datetime = models.DateTimeField(default=datetime.datetime.now(), blank=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField(blank=True, null=True)
	time_interaction = models.CharField(max_length=30, choices=TIME_CHOICES, default="LONG")