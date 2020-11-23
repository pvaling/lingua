from django.forms import Form, CharField, BooleanField


class CustomSignUpForm(Form):
    first_name = CharField()
    last_name = CharField()
    is_customer = BooleanField(required=False, label='I want to find Tutors', initial=True)
    is_tutor = BooleanField(required=False, label='I\'am a Tutor')

    def signup(self, request, user):
        user.is_customer = self.cleaned_data.get('is_customer')
        user.is_tutor = self.cleaned_data.get('is_tutor')
        user.save()
        pass
