from django.db import models
from .utils import create_shortend_url

# Create your models here.
class Shortener(models.Model):
    origin_url = models.URLField()
    short_url  = models.URLField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.origin_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortend_url(self)
            super().save(*args, **kwargs)