# Generated by Django 4.1.7 on 2023-10-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_objetives_miperfil_objectives_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miexamen',
            name='time_ans',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
