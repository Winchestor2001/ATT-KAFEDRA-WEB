# Generated by Django 4.1.2 on 2022-11-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_portfolio_portfolio_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_bg_pic',
            field=models.ImageField(blank=True, null=True, upload_to='subject_files/'),
        ),
    ]
