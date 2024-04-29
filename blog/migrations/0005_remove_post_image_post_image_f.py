# Generated by Django 5.0.3 on 2024-04-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_f',
            field=models.ImageField(blank=True, upload_to='blog_image'),
        ),
    ]
