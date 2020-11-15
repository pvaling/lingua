# Generated by Django 3.1.2 on 2020-11-14 19:58

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0003_auto_20201114_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euros')], default='EUR', editable=False, max_length=3),
        ),
    ]
