# Generated by Django 3.0.8 on 2020-08-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liftblog', '0004_homecarouseltext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpost',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
