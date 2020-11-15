# Generated by Django 3.1.2 on 2020-11-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0014_auto_20201115_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='tutor',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='tutors.Subject'),
        ),
    ]