from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from image_cropping import ImageRatioField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class User(AbstractUser):
    is_tutor = models.BooleanField('tutor status', default=False)
    is_customer = models.BooleanField('customer status', default=False)

    avatar = models.ImageField(blank=True, upload_to='uploaded_images')
    avatar_cropping = ImageRatioField('avatar', '430x360')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Tutor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    experience_years = models.IntegerField(blank=True, default=0)

    about = models.TextField(blank=True)

    price = MoneyField(
        blank=True, decimal_places=2, default_currency='EUR', max_digits=1000000,
        default=Money("0", "EUR")
    )

    is_available = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)

    def __str__(self):
        if self.user:
            display_name = self.user.first_name + " " + self.user.last_name
        else:
            display_name = 'User not set'
        return display_name



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Tutor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'tutor'):
        instance.tutor.save()

