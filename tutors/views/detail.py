from django.shortcuts import get_object_or_404, render
from django.views.decorators.clickjacking import xframe_options_sameorigin

from tutors.forms.new_chat_form import NewChatForm
from tutors.models import Tutor


@xframe_options_sameorigin
def detail(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=str(tutor_id))
    chat_form = NewChatForm(tutor=tutor)
    return render(request, 'tutors/detail.html', {'tutor': tutor, 'chat_form': chat_form})
