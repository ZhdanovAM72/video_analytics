# Generated by Django 4.2.7 on 2024-02-01 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check_list', '0007_rename_personnel_actions_checklist_personnel_actions_dict_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='personnel_actions_dict',
        ),
    ]