from allauth.account.forms import LoginForm
from django import forms


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

        # self.fields['password'].widget = forms.PasswordInput()
        #
        # # You don't want the `remember` field?
        # if 'remember' in self.fields.keys():
        #     del self.fields['remember']
        #
        # helper = FormHelper()
        # helper.form_show_labels = False
        # helper.layout = Layout(
        #     Field('login', placeholder='Email address'),
        #     Field('password', placeholder='Password'),
        #     FormActions(
        #         Submit('submit', 'Log me in to Cornell Forum', css_class='btn-primary')
        #     ),
        # )
        # self.helper = helper
