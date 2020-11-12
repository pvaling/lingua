from django.shortcuts import get_object_or_404, render

from teachers.models import Teacher

def detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=str(teacher_id))
    return render(request, 'teachers/detail.html', {'teacher': teacher})
