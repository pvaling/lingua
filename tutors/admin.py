from django.contrib import admin

# Register your models here.

from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Tutor, User, Language, Subject, ChatRoom

admin.site.register(Tutor)
admin.site.register(Language)
admin.site.register(Subject)
admin.site.register(ChatRoom)

class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
