# Generated by Django 3.2.4 on 2021-06-08 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beemaapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('New', 'New'), ('Active', 'Active'), ('Quoted', 'Quoted')], max_length=10)),
                ('type', models.CharField(choices=[('PA', 'Personal Accident'), ('LI', 'Life Insurance')], max_length=10)),
                ('premium', models.IntegerField()),
                ('cover', models.IntegerField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beemaapi.customer')),
            ],
        ),
    ]