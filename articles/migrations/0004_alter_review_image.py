# Generated by Django 3.2.13 on 2022-10-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
