# Generated by Django 3.1.3 on 2021-07-07 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresult',
            name='student_name',
        ),
    ]