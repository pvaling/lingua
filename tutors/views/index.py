
# Create your views here.

from tutors.models import Tutor
from django.shortcuts import render


def index(request):
    tutors = Tutor.objects.all()

    context = {
        'featured_tutors': tutors,
    }
    return render(request, 'tutors/index.html', context=context)
