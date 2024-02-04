from django.contrib import admin
from check_list.models import CheckList, PersonnelActions, PersonnelActionsValue

@admin.register(PersonnelActions)
class PersonnelActionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'personnel_action_description')
    fields = ('number', 'personnel_action_description')
    empty_value_display = '-данные отсутствуют-'


@admin.register(PersonnelActionsValue)
class PersonnelActionsValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_list_id', 'personnel_action', 'value', 'description')
    fields = ('check_list_id', 'personnel_action', 'value', 'description')
    list_filter = ('check_list_id',)
    empty_value_display = '-данные отсутствуют-'


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'video')
    fields = ('name', 'video', 'structural_subdivision',
              'working_place', 'record_date', 'bp_number',
              'working_person', 'controlling_person', 'recording_quality',
              'inspector', 'brif_conclusion', 'offer')
    empty_value_display = '-данные отсутствуют-'
