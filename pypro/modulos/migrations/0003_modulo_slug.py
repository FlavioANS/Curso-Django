# Generated by Django 4.0.3 on 2022-03-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_alter_modulo_options_modulo_descricao_modulo_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
