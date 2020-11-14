
from tutors.models import Tutor
from django.template import loader
from django.shortcuts import render, get_object_or_404


def register_tutor(request):

    # context = {
    #     'tutors': tutors,
    # }
    return render(request, 'tutors/tutor_register_form.html', context={})
