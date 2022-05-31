# Generated by Django 4.0.4 on 2022-05-31 14:04

from django.db import migrations, models
import finance_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0007_alter_stuff_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuffS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(default=finance_app.models.get_time)),
                ('month', models.DateTimeField(default=finance_app.models.get_month)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
