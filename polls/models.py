from django.db import models


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date publiched')


class Choice(models.Model):
	question = models.ForeignKey(Question, 'on_delete')
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)