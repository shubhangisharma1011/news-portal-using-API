# Generated by Django 3.2.5 on 2021-07-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0006_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='user_id',
        ),
    ]
