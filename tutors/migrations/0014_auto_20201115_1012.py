# Generated by Django 3.1.2 on 2020-11-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0013_auto_20201115_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='languages',
            field=models.ManyToManyField(blank=True, to='tutors.Language'),
        ),
    ]
