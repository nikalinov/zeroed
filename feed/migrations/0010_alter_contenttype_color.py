# Generated by Django 4.2.2 on 2023-07-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_alter_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('success', 'success'), ('warning', 'warning'), ('danger', 'danger')], default=('primary', 'primary'), max_length=20),
        ),
    ]
