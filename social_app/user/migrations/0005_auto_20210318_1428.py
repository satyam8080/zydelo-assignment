# Generated by Django 3.1.7 on 2021-03-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210318_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.CharField(default='noimg.jpg', editable=False, max_length=256),
        ),
    ]
