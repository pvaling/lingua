from django.contrib import admin

# Register your models here.

from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Tutor, User

admin.site.register(Tutor)

class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
