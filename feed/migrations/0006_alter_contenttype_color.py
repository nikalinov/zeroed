# Generated by Django 4.2.2 on 2023-07-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_userprofile_img_width_alter_contenttype_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('link', 'link'), ('success', 'success'), ('black', 'black'), ('dark', 'dark'), ('light', 'light'), ('white', 'white'), ('warning', 'warning'), ('danger', 'danger')], default=('success', 'success'), max_length=20),
        ),
    ]