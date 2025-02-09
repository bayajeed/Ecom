from django.db import models

# Create your models here.
class KeyValue(models.Model):
    key = models.CharField(max_length = 100)
    value = models.TextField()

    def __str__(self):
        return f'{self.key} : {self.value}'