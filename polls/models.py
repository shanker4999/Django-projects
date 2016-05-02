from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_test = models.TextField(max_length=255)
    pub_date = models.DateTimeField('date_published')

    def was_published_recently(selfself):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_test

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

