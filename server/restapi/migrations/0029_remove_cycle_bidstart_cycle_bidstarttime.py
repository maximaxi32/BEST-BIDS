# Generated by Django 4.1.2 on 2022-11-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('restapi', '0028_cycle_bidstart_cycle_maxprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='bidStart',
        ),
        migrations.AddField(
            model_name='cycle',
            name='bidStartTime',
            field=models.DateTimeField(null=True),
            preserve_default=False,
        ),
    ]