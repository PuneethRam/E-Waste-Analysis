# Generated by Django 3.2.16 on 2023-09-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20230921_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycle',
            name='claim_credit',
            field=models.IntegerField(null=True),
        ),
    ]
