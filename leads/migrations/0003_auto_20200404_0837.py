# Generated by Django 3.0.5 on 2020-04-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20200404_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
