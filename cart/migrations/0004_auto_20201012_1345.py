# Generated by Django 3.1.2 on 2020-10-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20201012_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='drive',
            field=models.BooleanField(default=False),
        ),
    ]
