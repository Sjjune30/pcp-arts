from django.db import models

# Create your models here.
class art(models.Model):
    image = models.ImageField(upload_to='sjimg')
    name = models.CharField(max_length=60)
    date = models.DateField()
    views = models.IntegerField()

    def __str__(self):
        return self.name