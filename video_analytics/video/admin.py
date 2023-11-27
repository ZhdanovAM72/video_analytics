from django.contrib import admin
from video.models import Group, Video, Status


# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description')
    # list_display = ('__all__',)
    empty_value_display = '-данные отсутствуют-'


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fields = ('name', 'color', 'slug',)
    # list_display = ('__all__',)
    empty_value_display = '-данные отсутствуют-'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    # fields = ('name', 'author', 'pub_date', 'description', 'status', 'video', 'image', 'group')
    list_display = ('name', 'author', 'pub_date', 'description', 'status', 'video', 'image', 'group')
    empty_value_display = '-данные отсутствуют-'
