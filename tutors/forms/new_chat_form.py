from django.forms import Form, ChoiceField, MultipleChoiceField, BooleanField, CharField, Textarea


class NewChatForm(Form):
    languages = ChoiceField(required=True)
    subjects = ChoiceField(required=True)

    description = CharField(required=False, widget=Textarea(attrs={'rows': 3}))

    is_public = BooleanField(required=False, label='Make available to other Tutors')

    def __init__(self, *args, **kwargs):
        tutor = kwargs.pop('tutor')
        super(NewChatForm, self).__init__(*args, **kwargs)
        self.fields['languages'] = MultipleChoiceField(choices=tuple([(x.id, x.label) for x in list(tutor.languages.all())]))
        self.fields['subjects'] = MultipleChoiceField(choices=tuple([(x.id, x.label) for x in list(tutor.subjects.all())]))
