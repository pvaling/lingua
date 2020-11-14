from django.shortcuts import render

from teachers.models import Teacher


def tutors_list(request):

    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
    }

    return render(request, 'teachers/list_page.html', context=context)
