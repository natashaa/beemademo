# Generated by Django 3.2.4 on 2021-06-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beemaapi', '0007_auto_20210609_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
