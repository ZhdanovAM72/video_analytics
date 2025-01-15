from django.urls import path

from check_list import views

app_name = 'check_list'


urlpatterns = [
    path('check_lists_info/', views.get_check_list_info, name='check_lists_info'),
    path('base_stats/', views.get_video_base_stats, name='base_stats'),
]
