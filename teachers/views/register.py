
from teachers.models import Teacher
from django.template import loader
from django.shortcuts import render, get_object_or_404


def register_teacher(request):

    # context = {
    #     'teachers': teachers,
    # }
    return render(request, 'teachers/register_teacher.html', context={})
