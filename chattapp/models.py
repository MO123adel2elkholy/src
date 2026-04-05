from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profileimg = models.ImageField(
        upload_to='profile', default='noprofile.png')
    friends = models.ManyToManyField('Friend', related_name="my_friends")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "friend"
        verbose_name_plural = "friends"

    def __str__(self):
        return self.profile.name


class ChattMessage(models.Model):
    body = models.TextField(max_length=100)
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender')
    reciver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='reciver')
    seen = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("ChattMessage")
        verbose_name_plural = ("ChattMessages")

    def __str__(self):
        return self.body
