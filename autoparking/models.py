from django.db import models

# Create your models here.
class thinkvision(models.Model):
    device_id=models.TextField(max_length=69,primary_key=True)
    slot1=models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    slot2=models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)

