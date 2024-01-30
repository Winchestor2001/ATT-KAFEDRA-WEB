# Generated by Django 4.1.2 on 2023-05-17 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kafedra", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articleviewip",
            name="ip",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="ArticleGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="articles/")),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kafedra.article",
                    ),
                ),
            ],
        ),
    ]
