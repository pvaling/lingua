from django import forms
from djmoney.forms import MoneyField, MoneyWidget


class CustomMoneyWidget(MoneyWidget):
    template_name = 'tutors/widgets/money.html'

class TutorProfileForm(forms.Form):

    first_name = forms.CharField(label='First name', max_length=100, disabled=True, required=False)
    last_name = forms.CharField(label='Last name', max_length=100, disabled=True, required=False)

    about = forms.CharField(label='About', widget=forms.Textarea)

    is_available = forms.BooleanField(required=False)
    is_approved = forms.BooleanField(required=False, disabled=True)

    experience_years = forms.IntegerField()
    price = MoneyField(default_currency='EUR', widget=CustomMoneyWidget)
