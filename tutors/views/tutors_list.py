from django.shortcuts import render

from tutors.filters.tutor_filter import TutorFilter
from tutors.models import Tutor


def tutors_list(request):

    filter = TutorFilter(request.GET, queryset=Tutor.objects.filter(is_approved=True, is_available=True))
    context = {
        'filter': filter,
        'active_nav': 'tutors'
    }

    return render(request, 'tutors/list_page.html', context=context)
