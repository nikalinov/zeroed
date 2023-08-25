# Generated by Django 4.2.2 on 2023-08-25 08:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0023_alter_blog_upvoters_alter_contenttype_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='upvoters',
            field=models.ManyToManyField(blank=True, related_name='upvoters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('success', 'success'), ('light', 'light'), ('warning', 'warning'), ('danger', 'danger')], default=('warning', 'warning'), max_length=20),
        ),
    ]
