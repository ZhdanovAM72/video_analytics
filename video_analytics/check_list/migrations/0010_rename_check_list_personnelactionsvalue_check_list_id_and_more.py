# Generated by Django 4.2.7 on 2024-02-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_list', '0009_alter_personnelactionsvalue_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnelactionsvalue',
            old_name='check_list',
            new_name='check_list_id',
        ),
        migrations.AlterField(
            model_name='personnelactionsvalue',
            name='value',
            field=models.CharField(blank=True, choices=[('ДА', 'ДА'), ('НЕТ', 'НЕТ')], help_text='Выбор из значений ДА/НЕТ', max_length=3, verbose_name='Отметка действия'),
        ),
    ]
