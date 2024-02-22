# Generated by Django 4.2.9 on 2024-02-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=160)),
                ('date_of_birth', models.DateField()),
                ('age', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=20)),
                ('full_address', models.CharField(max_length=260)),
                ('details', models.TextField()),
                ('patients_pic', models.ImageField(upload_to='patients')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]