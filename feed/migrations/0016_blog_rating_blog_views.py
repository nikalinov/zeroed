# Generated by Django 4.2.2 on 2023-07-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_alter_contenttype_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='rating',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
