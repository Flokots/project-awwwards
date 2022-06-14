from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from PIL import Image

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    landing_page = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    date_posted = models.DateTimeField(default=timezone.now)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
