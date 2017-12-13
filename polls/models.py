import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date publiched')

	def __str__(self):
		self.question_text

	def was_publiched_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question, 'on_delete')
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		self.choice_text