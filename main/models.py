from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    anons = models.TextField()
    image = models.FileField(upload_to='images')
    video = models.FileField(upload_to='video')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    
