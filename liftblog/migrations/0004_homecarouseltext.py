# Generated by Django 3.0.8 on 2020-08-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liftblog', '0003_videopost_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarouselText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
    ]
