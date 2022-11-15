# Generated by Django 4.1.2 on 2022-11-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_subject_subject_bg_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliocategory',
            name='portfolio_slug',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_file_1',
            field=models.FileField(blank=True, null=True, upload_to='subject_files/', verbose_name='Fan dasturi'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_file_2',
            field=models.FileField(blank=True, null=True, upload_to='subject_files/', verbose_name="Uslubiy ko'rsatma"),
        ),
    ]
