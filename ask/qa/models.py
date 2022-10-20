from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Model):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager() 
    title = models.CharField(max_length = 200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="q_to_u")
    likes = models.ManyToManyField(User, related_name="q_to_l")

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name="a_to_q")
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="a_to_u")
