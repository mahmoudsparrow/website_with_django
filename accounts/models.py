from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=140, default='')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=11, default='')
    image = models.ImageField(upload_to='profile_image', default='profile_image/19905311_469038166767229_3881908191928370159_n_oScytAS.jpg')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Chat(models.Model):
    user = models.ForeignKey(User)
    to_user = models.IntegerField()
    message = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
