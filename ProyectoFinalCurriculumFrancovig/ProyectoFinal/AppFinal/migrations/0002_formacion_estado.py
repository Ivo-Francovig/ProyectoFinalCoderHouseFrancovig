# Generated by Django 4.0.5 on 2022-07-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formacion',
            name='estado',
            field=models.CharField(default=(), max_length=40),
            preserve_default=False,
        ),
    ]
