# Generated by Django 4.1 on 2022-09-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_new_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='new_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
    ]
