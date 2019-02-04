from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 255)
    pub_date = models.DateTimeField('date created')

    def  __str__(self):
        return self.question_text

    def was_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 255)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

class Add(models.Model):
    comment = models.TextField(max_length=255)
    vote = models.IntegerField(max_length=10)

# Create your models here.
