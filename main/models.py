from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    anons = models.TextField()
    image = models.FileField(upload_to='images')
    video = models.FileField(upload_to='video')
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    
