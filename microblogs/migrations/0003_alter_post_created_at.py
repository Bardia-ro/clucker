# Generated by Django 3.2.8 on 2021-10-25 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0002_auto_20211025_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(blank=True),
        ),
    ]
