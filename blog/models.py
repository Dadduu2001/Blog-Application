from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image_f = models.ImageField(upload_to='blog_image', null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image_f.path)
        
    #     if img.height>300 or img.width>300:
    #         output = (300, 300)
    #         img.thumbnail(output)
    #         img.save(self.image_f.path)
    