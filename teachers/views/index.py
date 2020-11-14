
# Create your views here.

from teachers.models import Teacher
from django.shortcuts import render


def index(request):
    teachers = Teacher.objects.all()

    context = {
        'featured_teachers': teachers,
    }
    return render(request, 'teachers/index.html', context=context)
