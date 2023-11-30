# Generated by Django 4.2.5 on 2023-11-26 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_customuser_email_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Worker_Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mande_app.job')),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('hours', models.IntegerField()),
                ('cost', models.FloatField()),
                ('rating', models.FloatField(null=True)),
                ('description', models.TextField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
                ('worker_job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mande_app.worker_job')),
            ],
        ),
    ]