from django.db import models
from django.utils.text import slugify


TAGS = (
  ('Tech', 'Tech'),
  ('General', 'General'),
  ('Life', 'Life')
)

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
  description = models.CharField(max_length=500)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  tag = models.CharField(max_length=50, choices=TAGS, default='General')
  # image = models.ImageField(upload_to='post_images/')

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

# TODO: comments section