from django.db import models

# Create your models here.


class URL(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link
