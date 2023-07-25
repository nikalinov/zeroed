# Generated by Django 4.2.2 on 2023-07-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_contenttype_color_alter_userprofile_reputation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('link', 'link'), ('success', 'success'), ('black', 'black'), ('dark', 'dark'), ('light', 'light'), ('white', 'white'), ('warning', 'warning'), ('danger', 'danger')], default=('success', 'success'), max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='feed/profile-pics/user-default.svg', upload_to='feed/profile-pics/', width_field='img_width'),
        ),
    ]