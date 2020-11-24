from django.forms import Form, CharField, ChoiceField, RadioSelect


class CustomSignUpForm(Form):
    first_name = CharField()
    last_name = CharField()

    role = ChoiceField(choices=(
        ('is_customer', 'Parent'), ('is_tutor', 'Tutor'), ('is_school', 'School')),
        widget=RadioSelect)

    def signup(self, request, user):
        user.is_customer = self.cleaned_data.get('role') == 'is_customer'
        user.is_tutor = self.cleaned_data.get('role') == 'is_tutor'
        user.is_school = self.cleaned_data.get('role') == 'is_school'
        user.save()
        pass
