from django.db import models

class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
