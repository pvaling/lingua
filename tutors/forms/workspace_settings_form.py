from django.forms import Form, ChoiceField


class WorkspaceSettingsForm(Form):
    user_type = ChoiceField(choices=(
        ('customer', 'Parent'),
        ('tutor', 'Tutor'),
        ('school', 'School'),
    ), required=True)
