import logging

from django import forms
from django.forms import inlineformset_factory
from check_list.models import (
    CheckList, PersonnelActions, PersonnelActionsValue
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)


class PersonnelActionsValueForm(forms.ModelForm):
    check_list_id = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    class Meta:
        model = PersonnelActionsValue
        fields = ['value', 'description', 'check_list_id', 'personnel_action']

    def is_valid(self):
        return True


class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        exclude = ['personnel_actions_dict']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        personnel_actions_dict = PersonnelActions.objects.all()
        check_list_instance = CheckList.objects.last()

        PersonnelActionsValueFormSet = inlineformset_factory(
            CheckList,
            PersonnelActionsValue,
            form=PersonnelActionsValueForm,
            extra=len(personnel_actions_dict),
            can_delete=False,
        )

        initial_data = [
            {
                'personnel_action': pa.id,
                'value': 'ДА',
                'description': '...'
            } for pa in personnel_actions_dict
        ]

        self.formset = PersonnelActionsValueFormSet(
            instance=check_list_instance,
            queryset=PersonnelActionsValue.objects.none(),
            prefix='personnelactionsvalue_set',  # добавлен префикс
            initial=initial_data,
        )

        # Добавлены скрытые поля для передачи значений
        for i, formset_form in enumerate(self.formset.forms):
            self.fields[f'personnelactionsvalue_set-{i}-value'] = forms.CharField(widget=forms.HiddenInput())
            self.fields[f'personnelactionsvalue_set-{i}-description'] = forms.CharField(widget=forms.HiddenInput())
            self.fields[f'personnelactionsvalue_set-{i}-personnel_action'] = forms.IntegerField(widget=forms.HiddenInput())

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        logging.info(f'CheckListForm - Save: {instance}')
        return instance
