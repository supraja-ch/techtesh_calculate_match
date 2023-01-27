from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name=models.CharField(max_length=56)
    last_name=models.CharField(max_length=56)
    email_address=models.EmailField()
    profile_picture = models.ImageField(default='default.jpg',upload_to='teacher')
    mobile_number=models.CharField(max_length=16)
    room_number = models.CharField(max_length=10)
    subject_taught = models.CharField(max_length=256)
    # subject_count= models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.first_name


       
