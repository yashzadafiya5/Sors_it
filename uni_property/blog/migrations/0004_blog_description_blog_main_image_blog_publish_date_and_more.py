# Generated by Django 4.0.5 on 2023-03-01 12:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_description_remove_blog_main_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='jfbwejbwfjbfkwbfjw'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(default='abc', upload_to='blog_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default='2023-03-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='abc', max_length=180),
            preserve_default=False,
        ),
    ]