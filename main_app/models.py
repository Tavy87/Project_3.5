from django.db import models
from django.urls import reverse

class Widget(models.Model):
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.description} {self.quantity}'

    def get_absolute_url(self):
        return reverse('index', kwargs={'widget_id': self.id})
