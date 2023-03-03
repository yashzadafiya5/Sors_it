from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name=models.TextField(max_length=120)
    mobile=models.BigIntegerField()
    email=models.TextField()
    subject=models.TextField()
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True) 