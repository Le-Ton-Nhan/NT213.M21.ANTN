# Generated by Django 3.2.8 on 2021-11-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0035_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='monhoc',
            name='tenMH_search',
            field=models.CharField(default='djangodbmodelsfieldscharfield', max_length=150),
        ),
    ]
