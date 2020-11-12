
# Create your views here.

from django.http import HttpResponse, JsonResponse

from teachers.models import Teacher
from django.template import loader
from django.shortcuts import render, get_object_or_404


def index(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
    }
    return render(request, 'teachers/index.html', context=context)

