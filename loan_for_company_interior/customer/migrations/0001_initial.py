# Generated by Django 4.1.6 on 2023-02-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('enquiry_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('Successful', 'Successful'), ('rejected', 'rejected')], default='', max_length=50)),
                ('response_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
