# Generated by Django 3.2.9 on 2022-10-28 22:59

import datetime
from django.db import migrations, models
import food_tickets.utils


class Migration(migrations.Migration):

    dependencies = [
        ('food_tickets', '0008_remove_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodaccesslog',
            options={'verbose_name': 'Использованный талончик', 'verbose_name_plural': 'Использованные талончики'},
        ),
        migrations.AlterModelOptions(
            name='foodticket',
            options={'verbose_name': 'Талончик', 'verbose_name_plural': 'Талончики'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=datetime.datetime(2022, 10, 29, 1, 59, 5, 584590)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(max_length=256, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='student',
            name='secret_code',
            field=models.CharField(blank=True, default=food_tickets.utils.random_secret_code, max_length=256, null=True, verbose_name='Секретный код ученика'),
        ),
    ]
