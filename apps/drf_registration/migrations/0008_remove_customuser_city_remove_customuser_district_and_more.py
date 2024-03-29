# Generated by Django 4.2.4 on 2023-08-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_registration', '0007_customuser_show_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='district',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='institution_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='show_contact',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('parttime', 'Part-Time'), ('fulltime', 'Full-Time')], default='parttime', max_length=20),
        ),
    ]
