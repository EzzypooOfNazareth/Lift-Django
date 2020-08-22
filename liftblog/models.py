from django.db import models
from django.contrib.auth.models import User

class TextPost(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class VideoPost(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_video = models.FileField(upload_to='videos/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HomeCarousel(models.Model):
    image = models.ImageField(upload_to='homeCarouselImages/')

class HomeCarouselText(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text
