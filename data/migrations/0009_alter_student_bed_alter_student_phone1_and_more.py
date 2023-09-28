# Generated by Django 4.2.2 on 2023-08-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_student_bed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone1',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone2',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='place',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
