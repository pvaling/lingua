from django import forms
from django.forms import ImageField
from djmoney.forms import MoneyField, MoneyWidget
from image_cropping import ImageCropField, ImageCropWidget, ImageRatioField

from tutors.models import User



class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'cropping')


class TutorProfileForm(forms.Form):

    first_name = forms.CharField(label='First name', max_length=100, disabled=True, required=False)
    last_name = forms.CharField(label='Last name', max_length=100, disabled=True, required=False)

    about = forms.CharField(label='About', widget=forms.Textarea(attrs={'rows':4}))

    is_available = forms.BooleanField(required=False)
    is_approved = forms.BooleanField(required=False, disabled=True)

    experience_years = forms.IntegerField()
    price = MoneyField(default_currency='EUR')


class TutorGalleryForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
