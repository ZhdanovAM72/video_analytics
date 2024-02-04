from django.contrib import admin
from check_list.models import (
    CheckList, PersonnelActions, PersonnelActionsValue
)

@admin.register(PersonnelActions)
class PersonnelActionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'personnel_action_description')
    fields = ('number', 'personnel_action_description')
    empty_value_display = '-данные отсутствуют-'


@admin.register(PersonnelActionsValue)
class PersonnelActionsValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_list_id', 'personnel_action',
                    'value', 'description')
    fields = ('check_list_id', 'personnel_action', 'value', 'description')
    list_filter = ('value',)
    empty_value_display = '-данные отсутствуют-'


class PersonnelActionsValueInline(admin.StackedInline):
    model = PersonnelActionsValue
    extra = 0


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    inlines = [PersonnelActionsValueInline]
    list_display = ('id', 'name', 'video', 'get_yes', 'get_no')
    fields = ('name', 'video', 'structural_subdivision',
              'working_place', 'record_date', 'bp_number',
              'working_person', 'controlling_person', 'recording_quality',
              'inspector', 'brif_conclusion', 'offer')
    empty_value_display = '-данные отсутствуют-'

    def get_yes(self, obj):
        return PersonnelActionsValue.objects.filter(
            check_list_id=obj, value='ДА'
        ).count()
    get_yes.short_description = 'Количество верных действий'

    def get_no(self, obj):
        return PersonnelActionsValue.objects.filter(
            check_list_id=obj, value='НЕТ'
        ).count()
    get_no.short_description = 'Количество ошибок'
