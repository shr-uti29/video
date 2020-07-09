from django.db import models


from django.contrib.auth.models import User

#Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Contact = models.CharField(max_length=20,null=False,blank=False)
    Address = models.CharField(max_length=100,null=False,blank=False)
    
    def __str__(self):
        return "{0}".format(self.user.username)