# Generated by Django 3.1.2 on 2020-11-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
