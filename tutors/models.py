from django.db import models

# Create your models here.
from djmoney.models.fields import MoneyField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class Tutor(models.Model):
    firstname = models.CharField(max_length=1024)
    lastname = models.CharField(max_length=1024)
    email = models.EmailField(blank=False)

    avatar_file = models.FileField(blank=True, upload_to=user_directory_path)

    experience_years = models.IntegerField(blank=True, default=0)

    about = models.TextField(blank=True)

    price = MoneyField(blank=True, decimal_places=2, default=0, default_currency='EUR', max_digits=1000000)

    def __str__(self):
        return self.firstname + " " + self.lastname
