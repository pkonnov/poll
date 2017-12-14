import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date publiched')

	def __str__(self):
		return self.question_text

	def was_publiched_recently(self): #published:)
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		was_publiched_recently.admin_order_field = 'pub_date'
		was_publiched_recently.boolean = True
		was_publiched_recently.chort_description = 'Недавно опубликован?'


class Choice(models.Model):
	question = models.ForeignKey(Question, 'on_delete')
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text