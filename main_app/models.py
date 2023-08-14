from django.db import models

class Widget(models.Model):
    decription = models.CharField(max_length=250)
    quanitity = models.IntegerField()
    def __str__(self):
        return self.decription