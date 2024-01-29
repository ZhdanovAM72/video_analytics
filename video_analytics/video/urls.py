from django.urls import path

from video import views

app_name = 'video'


urlpatterns = [
    # Для открытия видео отдельно
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('<int:pk>/', views.get_video, name='video'),
    # path('', views.get_list_video, name='index'),
    path('', views.index, name='index'),
]
