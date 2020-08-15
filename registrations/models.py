from django.db import models

from datetime import datetime

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

DURATION_CHOICES = [
    ('SHORT', 'Short'),
    ('MEDIUM', 'Medium'),
    ('LONG', 'Long'),
]


PERS_AGE_CHOICES = [(i,i) for i in range(16, 46)]

RATING_CHOICES = [(i,i) for i in range(1, 11)]


class Person(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	title = models.CharField(max_length=30, choices=TITLE_CHOICES, default='NA')
	pers_age = models.IntegerField(choices=PERS_AGE_CHOICES, default=18)
	duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default='NA')
	rating = models.IntegerField(choices=RATING_CHOICES, default=5)

	def __str__(self):
		return self.first_name