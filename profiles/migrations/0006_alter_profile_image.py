# Generated by Django 3.2.18 on 2023-03-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_post_tegyto', upload_to='images/'),
        ),
    ]
