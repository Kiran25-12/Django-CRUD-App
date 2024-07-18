# Generated by Django 4.2.11 on 2024-07-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('department', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]