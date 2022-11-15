# Generated by Django 4.1.2 on 2022-11-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_alter_subject_subject_file_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('context', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_file',
            field=models.FileField(upload_to='portfolio_files/'),
        ),
    ]
