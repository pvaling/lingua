from django.urls import path

from .views.detail import detail
from .views.index import index

app_name = 'teachers'

urlpatterns = [
    path('', index, name='index'),
    path('teacher/<int:teacher_id>', detail, name='detail'),
]
