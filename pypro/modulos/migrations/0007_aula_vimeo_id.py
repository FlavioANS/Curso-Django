# Generated by Django 4.0.3 on 2022-03-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]