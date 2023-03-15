# Generated by Django 4.1 on 2023-03-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('brief_information', models.CharField(max_length=50)),
                ('profile_information', models.CharField(max_length=1000)),
                ('scientific_degree', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Dermatologist',
        ),
        migrations.DeleteModel(
            name='General_Health_Doctor',
        ),
        migrations.DeleteModel(
            name='Gynecologist',
        ),
        migrations.DeleteModel(
            name='Naturopathist',
        ),
        migrations.DeleteModel(
            name='Psychiatrist',
        ),
    ]
