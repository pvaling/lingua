from django.shortcuts import get_object_or_404, render

from tutors.models import Tutor

def detail(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=str(tutor_id))
    return render(request, 'tutors/detail.html', {'tutor': tutor})
