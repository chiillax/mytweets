# Generated by Django 2.0.9 on 2018-12-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='tweet',
            new_name='tweets',
        ),
    ]
