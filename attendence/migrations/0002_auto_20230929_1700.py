# Generated by Django 3.2.18 on 2023-09-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='mob1',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='attendence',
            name='mob2',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
