# Generated by Django 4.0.5 on 2022-06-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_project_landing_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='landing_page',
            field=models.ImageField(default='default_land.jpg', upload_to='landing_pages/'),
        ),
    ]