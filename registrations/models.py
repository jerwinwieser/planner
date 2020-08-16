
"""
name
age
nationality
duration interaction
grade interaction
grade looks
comments
number close
chat reply
date
lay
"""


from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

DURATION_CHOICES = [
    ('SHORT', 'Short'),
    ('MEDIUM', 'Medium'),
    ('LONG', 'Long'),
]

# PERS_AGE_CHOICES = [(i,i) for i in range(16, 46)]

# RATING_CHOICES = [(i,i) for i in range(1, 11)]


class Person(models.Model):
	name = models.CharField(max_length=30)
	duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default='NA')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	
	def __str__(self):
		return str(self.id)
