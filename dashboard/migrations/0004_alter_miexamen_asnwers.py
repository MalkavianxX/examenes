# Generated by Django 4.1.7 on 2023-10-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0002_alter_pregunta_imgage'),
        ('dashboard', '0003_alter_miexamen_time_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miexamen',
            name='asnwers',
            field=models.ManyToManyField(blank=True, null=True, to='examenes.respuesta'),
        ),
    ]
