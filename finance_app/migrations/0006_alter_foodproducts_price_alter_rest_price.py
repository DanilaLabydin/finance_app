# Generated by Django 4.0.4 on 2022-05-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0005_stuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodproducts',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rest',
            name='price',
            field=models.IntegerField(),
        ),
    ]
