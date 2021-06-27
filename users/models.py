from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField('birthday')
    gender = models.CharField(choices=(('male', '男性'),('female', '女性')), max_length=10)
    def __str__(self):
        return self.name
    def get_absolute_url(self): 
        return reverse('user_detail', args=[str(self.id)])