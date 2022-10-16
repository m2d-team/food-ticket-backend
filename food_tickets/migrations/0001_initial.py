# Generated by Django 3.2.9 on 2022-10-16 17:21

from django.db import migrations, models
import django.db.models.deletion
import food_tickets.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20221016_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('date_of_birth', models.CharField(max_length=256)),
                ('grade', models.CharField(max_length=8)),
                ('secret_code', models.CharField(default=food_tickets.utils.random_secret_code, max_length=256)),
                ('telegram_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.telegramuser')),
            ],
        ),
        migrations.CreateModel(
            name='FoodAccessLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_tickets.student')),
            ],
        ),
    ]