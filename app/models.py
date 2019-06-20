from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):      
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to='profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)

    # Foreign Key
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Assets(models.Model):
    name = models.CharField(max_length=60)
    assetfile = models.FileField(upload_to='media/')
    date_time = models.DateTimeField(auto_now_add=True)

    # Foreign Key
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_time

