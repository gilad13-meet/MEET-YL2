from django.db import models

# Create your models(classes) here.
class Poll(models.Model):
	question = Models.CharField(max_length=200)
class Choice(models.Model):
	choice = Models.CharField(max_length=200)]
	poll = models.FoteignKey(Poll)	