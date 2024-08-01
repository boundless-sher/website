from django.db import models
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files import File



def image_compression(image):
  img = Image.open(image)
  img = img.convert('RGB')
  img_io = BytesIO()
  img.save(img_io, 'JPEG', quality=60, optimize=True)
  new_image = File(img_io, name=image.name)
  return new_image 


# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField(blank=True, null=True, default='')
  url = models.CharField(max_length=300)
  image = models.ImageField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def save(self, *args, **kwargs):
    self.image = image_compression(self.image)
    super().save(*args, **kwargs)



  def __str__(self):
    return self.title