from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import social_account_added
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from image_cropping import ImageRatioField, ImageCropField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)





class User(AbstractUser):

    is_tutor = models.BooleanField('tutor status', default=False)
    is_customer = models.BooleanField('customer status', default=False)

    avatar = ImageCropField(blank=True, upload_to='uploaded_images')
    cropping = ImageRatioField('avatar', '430x360')

    def __str__(self):
        return self.first_name + ' ' + self.last_name




class Language(models.Model):
    label = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.label

class Subject(models.Model):
    label = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.label

class Tutor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    experience_years = models.IntegerField(blank=True, default=0)

    about = models.TextField(blank=True)

    price = MoneyField(
        blank=True, decimal_places=2, default_currency='EUR', max_digits=1000000,
        default=Money("0", "EUR")
    )

    languages = models.ManyToManyField(Language, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    is_available = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)

    def __str__(self):
        if self.user:
            display_name = self.user.first_name + " " + self.user.last_name
        else:
            display_name = 'User not set'
        return display_name


class GalleryItem(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_items')
    order = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created, **kwargs):
    # if created:
    #     Tutor.objects.create(user=instance)
    #     instance.is_tutor = True
    #     instance.save()
    pass

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_tutor:

        if not hasattr(instance, 'tutor'):
            Tutor.objects.create(user=instance)

        instance.tutor.save()


class ChatRoom(models.Model):
    members = models.ManyToManyField(User)

    def __str__(self):
        return 'Chat_id:{chat_id}'.format(chat_id=self.id) + '/' + '<->'.join([str(x.id) for x in self.members.all()])


class ChatMessage(models.Model):

    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    body = models.CharField(max_length=10000)

    attachment = models.FileField(upload_to='chat_attachments', blank=True)
