# Generated by Django 4.0.5 on 2022-07-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0003_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='formacion',
            name='descripcion',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
