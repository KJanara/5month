from django.db import models


class Movie(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField()
  duration = models.PositiveIntegerField()


  def __str__(self):
    return self.title

