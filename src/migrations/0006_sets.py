# Generated by Django 3.1.2 on 2020-12-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20201211_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_image', models.ImageField(upload_to='setting_images')),
                ('g_image', models.ImageField(upload_to='setting_images')),
            ],
        ),
    ]
