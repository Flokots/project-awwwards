from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    landing_page = models.ImageField(default='default_land.jpg', upload_to='landing_pages/')
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

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)

        return projects


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    usability_rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    content_rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.project.title}'
