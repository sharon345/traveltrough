from django.db import models

# Create your models here.


class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    disc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    #   name=models.CharField(max_length==200)
    # img=models.ImageField(upload_to='images')
    # disc=models.TextField()
