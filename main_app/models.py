from django.db import models


class Widget(models.Model):
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return (f'{self.description} {self.quantity}')