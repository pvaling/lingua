# Generated by Django 3.1.2 on 2020-11-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0002_auto_20201121_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_school',
            field=models.BooleanField(default=False, verbose_name='school status'),
        ),
    ]