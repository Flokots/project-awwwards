# Generated by Django 4.0.5 on 2022-06-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_user.jpg', upload_to='profile_pics/'),
        ),
    ]
