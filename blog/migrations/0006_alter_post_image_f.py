# Generated by Django 5.0.3 on 2024-04-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_image_post_image_f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_f',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image'),
        ),
    ]
