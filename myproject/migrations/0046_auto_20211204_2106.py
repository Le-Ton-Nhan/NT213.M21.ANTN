# Generated by Django 3.2.8 on 2021-12-04 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myproject', '0045_alter_commenttl_matl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmh',
            name='MaMH',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myproject.monhoc'),
        ),
        migrations.AlterField(
            model_name='commentmh',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsMH', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commenttl',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsTL', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='informationuser',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recentview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tailieu',
            name='MaMH',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='monhoc', to='myproject.monhoc'),
        ),
        migrations.AlterField(
            model_name='thongbao',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thongbao', to=settings.AUTH_USER_MODEL),
        ),
    ]
