# Generated by Django 4.2.2 on 2023-08-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0021_alter_blog_picture_alter_contenttype_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('success', 'success'), ('light', 'light'), ('warning', 'warning'), ('danger', 'danger')], default=('primary', 'primary'), max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='feed/profile-pics/profile-default.jpg', upload_to='feed/profile-pics/', width_field='img_width'),
        ),
    ]