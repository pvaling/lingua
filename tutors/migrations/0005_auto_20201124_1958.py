# Generated by Django 3.1.2 on 2020-11-24 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0004_auto_20201121_1949'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobRequest',
            new_name='JobOffer',
        ),
    ]