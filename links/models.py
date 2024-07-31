from django.db import models

# Create your models here.
class Link(models.Model):
  title = models.CharField(max_length=100)
  url = models.URLField()
  description = models.TextField(blank=True, null=True, default='')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title