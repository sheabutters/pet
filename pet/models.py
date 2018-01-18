from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.


class Pet(models.Model):
    nickname = models.CharField(max_length=12, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('pet:pet_detail', args=[self.id])

    @property
    def mng_log(self):
        how_many_days = 3
        mng_info = {
            'food': self.mnglog_set.filter(type='food', created_date__gte=datetime.now()-timedelta(days=how_many_days)).count(),
            'clea': self.mnglog_set.filter(type='clea', created_date__gte=datetime.now()-timedelta(days=how_many_days)).count(),
            'play': self.mnglog_set.filter(type='play', created_date__gte=datetime.now()-timedelta(days=how_many_days)).count(),
            'trai': self.mnglog_set.filter(type='trai').count()
        }
        return mng_info


# food, play, clea, trai


class MngLog(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=4, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

