from django.db import models

from datetime import datetime

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]


class Person(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	title = models.CharField(max_length=3, choices=TITLE_CHOICES, default='NA')


	def __str__(self):
		return self.first_name