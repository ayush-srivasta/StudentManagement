# Generated by Django 3.2.4 on 2021-10-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_marks_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='marks',
        ),
    ]
