# Generated by Django 2.2.5 on 2019-12-03 01:15

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20191202_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='cover',
            field=sorl.thumbnail.fields.ImageField(height_field='cover_h', upload_to='', verbose_name='couverture', width_field='cover_w'),
        ),
    ]
