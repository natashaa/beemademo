# Generated by Django 3.2.4 on 2021-06-09 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beemaapi', '0002_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('T', 'Transgender')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='beemaapi.customer'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='state',
            field=models.CharField(choices=[('new', 'New'), ('quoted', 'Quoted'), ('bound', 'Bound')], default='new', max_length=10),
        ),
    ]