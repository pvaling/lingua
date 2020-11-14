from django.urls import path

from .views.tutors_list import tutors_list
from .views.detail import detail
from .views.index import index
from .views.register import register_tutor
from .views.tutor_profile import tutor_profile

app_name = 'tutors'

urlpatterns = [
    path('', index, name='index'),
    path('tutor/<int:tutor_id>', detail, name='detail'),
    path('tutor/register', register_tutor, name='register_tutor'),
    path('tutor/profile', tutor_profile, name='tutor_profile'),
    path('tutors/list', tutors_list, name='tutors_list'),
]
