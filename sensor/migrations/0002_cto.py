# Generated by Django 5.0.4 on 2024-05-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255)),
                ('service_code', models.CharField(max_length=255)),
            ],
        ),
    ]
