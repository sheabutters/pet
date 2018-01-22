from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
import pytz
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Pet(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    nickname = models.CharField(max_length=12, null=False, default="이름없음")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('pet:pet_detail', args=[self.id])

    @property
    def mng_log(self):
        HOW_MANY_DAYS = 3
        tz=pytz.timezone('Asia/Seoul')
        mng_info = {
            'food': self.mnglog_set.filter(type='food', created_date__gte=datetime.now(tz)-timedelta(days=HOW_MANY_DAYS)).count(),
            'clea': self.mnglog_set.filter(type='clea', created_date__gte=datetime.now(tz)-timedelta(days=HOW_MANY_DAYS)).count(),
            'play': self.mnglog_set.filter(type='play', created_date__gte=datetime.now(tz)-timedelta(days=HOW_MANY_DAYS)).count(),
            'trai': self.mnglog_set.filter(type='trai').count()
        }
        return mng_info

    @property
    def age(self):
        d = self.created_date.timestamp()
        now = datetime.now(tz=pytz.timezone('Asia/Seoul')).timestamp()
        since = int((now - d)/60/60)
        return since


@receiver(post_save, sender=User)
def create_user_pet(sender, instance, created, **kwargs):
    if created:
        Pet.objects.create(owner=instance)

@receiver(post_save, sender=User)
def save_user_pet(sender, instance, **kwargs):
    instance.pet.save()
    

# food, play, clea, trai

class MngLog(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=4, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

