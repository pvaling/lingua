
# Create your views here.

from tutors.models import Tutor
from django.shortcuts import render


def index(request):
    tutors = Tutor.objects.all().filter(is_available=True, is_approved=True)

    context = {
        'featured_tutors': tutors,
    }
    return render(request, 'tutors/index.html', context=context)
