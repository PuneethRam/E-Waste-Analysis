# Generated by Django 3.2.16 on 2023-09-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20230920_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycle',
            name='stage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recycle',
            name='device_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
