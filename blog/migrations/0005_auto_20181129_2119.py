# Generated by Django 2.1.3 on 2018-11-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]