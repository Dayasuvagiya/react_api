# Generated by Django 3.2.3 on 2023-10-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_dph0lu', upload_to='images/'),
        ),
    ]
