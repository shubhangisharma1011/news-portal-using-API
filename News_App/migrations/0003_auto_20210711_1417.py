# Generated by Django 3.2.5 on 2021-07-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0002_alter_comment_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
