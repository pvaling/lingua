from django.urls import path

from .views.tutor_chat import tutor_chat, tutor_chatrooms, chatroom
from .views.tutor_profile_gallery import tutor_profile_gallery
from .views.user_profile import user_profile
from .views.tutors_list import tutors_list
from .views.detail import detail
from .views.index import index
from .views.register import register_tutor
from .views.workspace import workspace_index, workspace_settings, workspace_tutor_profile_edit, \
    OrderList, OrderDetailView, OrderDelete

app_name = 'tutors'


urlpatterns = [
    path('', index, name='index'),
    path('tutor/<int:tutor_id>', detail, name='detail'),
    path('tutor/<int:tutor_id>/chat', tutor_chat, name='tutor_chat'),
    path('tutor/chatrooms', tutor_chatrooms, name='tutor_chatrooms'),
    path('chatroom/<int:chatroom_id>', chatroom, name='chatroom'),
    path('tutor/register', register_tutor, name='register_tutor'),
    path('tutor/profile/avatar', user_profile, name='tutor_profile_avatar'),
    path('tutor/profile/gallery', tutor_profile_gallery, name='tutor_profile_gallery'),
    path('user_profile', user_profile, name='user_profile'),
    path('tutors/list', tutors_list, name='tutors_list'),
    path('workspace', workspace_index, name='workspace_index'),
    path('workspace/settings', workspace_settings, name='workspace_settings'),
    path('workspace/orders_list', OrderList.as_view(), name='workspace_orders_list'),
    path('workspace/order/<int:pk>', OrderDetailView.as_view(), name='workspace_order_detail'),
    path('workspace/order/<int:pk>/delete', OrderDelete.as_view(), name='workspace_order_delete'),
    path('workspace/tutor_profile_edit', workspace_tutor_profile_edit, name='workspace_tutor_profile_edit'),
]
