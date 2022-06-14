from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    landing_page = models.ImageField(upload_to='landing_pages/')
    date_posted = models.DateTimeField(default=timezone.now)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.landing_page.path)

        if img.height > 940 or img.width > 960:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.landing_page.path)

       
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
