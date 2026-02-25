from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=400)
    summary=models.TextField()
    image=models.ImageField()
    price=models.FloatField()
    working_days=models.DateTimeField()





