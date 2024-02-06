from django.contrib import admin
from django.utils.safestring import mark_safe

from video.models import Group, Video, Status
from check_list.models import CheckList


# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description')
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-данные отсутствуют-'


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fields = ('name', 'color', 'slug',)
    list_display = ('id', 'name', 'color')
    empty_value_display = '-данные отсутствуют-'


class CheckListInline(admin.StackedInline):
    model = CheckList
    extra = 0


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [CheckListInline]
    list_display = ('name', 'author', 'pub_date', 'description',
                    'status', 'video', 'get_html_image', 'group')
    empty_value_display = '-данные отсутствуют-'

    def get_html_image(self, obj):
        """Делаем картинки в админке видимыми."""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50>')
    get_html_image.short_description = 'Картинка'
