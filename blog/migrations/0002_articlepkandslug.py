# Generated by Django 2.1.7 on 2019-02-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="ArticlePkAndSlug",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(default="", editable=False, max_length=100)),
            ],
        )
    ]
