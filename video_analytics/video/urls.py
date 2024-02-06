from django.urls import path

from video import views

app_name = 'video'


urlpatterns = [
    # Для открытия видео отдельно
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('video/<int:pk>/', views.get_video, name='video'),
    path('video/create/', views.create_video, name='create_video'),
    # path('<int:pk>/', views.VideoDetailView, name='video'),
    path('new/', views.new_index, name='new_index'),
    path('done/', views.done_index, name='done_index'),
    # path('', views.get_list_video, name='index'),
    path('', views.index, name='index'),
]
