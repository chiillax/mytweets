# Generated by Django 2.0.9 on 2018-12-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
