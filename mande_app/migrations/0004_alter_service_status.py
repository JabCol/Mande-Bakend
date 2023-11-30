# Generated by Django 4.2.5 on 2023-11-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mande_app', '0003_worker_job_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('F', 'Finished'), ('C', 'Canceled')], default='A', max_length=1),
        ),
    ]