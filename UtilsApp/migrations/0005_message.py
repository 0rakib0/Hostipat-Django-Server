# Generated by Django 5.0.2 on 2024-03-01 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0001_initial'),
        ('UtilsApp', '0004_notise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('readStatus', models.BooleanField(default=False)),
                ('creatAt', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctors.doctor')),
            ],
        ),
    ]