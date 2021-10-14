# Generated by Django 3.2.4 on 2021-10-07 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_studentprofile_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta1', models.IntegerField(default=0)),
                ('ta2', models.IntegerField(default=0)),
                ('ta3', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='users.department'),
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.AddField(
            model_name='subject',
            name='marks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.marks'),
        ),
    ]
