from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField(blank=True, null=True, default='')
  url = models.CharField(max_length=300)
  image = models.ImageField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title