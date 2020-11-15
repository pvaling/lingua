from django.shortcuts import render

from tutors.models import Tutor


def tutors_list(request):

    tutors = Tutor.objects.filter(is_approved=True, is_available=True)

    context = {
        'tutors': tutors,
    }

    return render(request, 'tutors/list_page.html', context=context)
