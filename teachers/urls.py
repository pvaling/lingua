from django.urls import path

from .views.tutors_list import tutors_list
from .views.detail import detail
from .views.index import index
from .views.register import register_teacher

app_name = 'teachers'

urlpatterns = [
    path('', index, name='index'),
    path('teacher/<int:teacher_id>', detail, name='detail'),
    path('teacher/register', register_teacher, name='register_teacher'),
    path('tutors/list', tutors_list, name='tutors_list'),
]
