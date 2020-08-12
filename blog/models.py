from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('画像', upload_to = 'images', blank=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()
        self.updated_at =  timezone.now()

    def __str__(self):
        return self.title
