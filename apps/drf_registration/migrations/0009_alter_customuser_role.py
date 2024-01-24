# Generated by Django 4.2.4 on 2023-08-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_registration', '0008_remove_customuser_city_remove_customuser_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('parttime', 'Part-Time'), ('fulltime', 'Full-Time'), ('admin', 'Admin')], default='parttime', max_length=20),
        ),
    ]
