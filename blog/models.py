from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')
    image_medium = ImageSpecField(source='image',
                                  processors=[Thumbnail(200, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(100, 50)],
                                 format='JPEG',
                                 options={'quality': 60})
    slug = models.SlugField(max_length=255, unique=True)py

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        self.updated_at =  timezone.now()

    def __str__(self):
        return self.title