# Generated by Django 4.2.6 on 2023-11-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0007_authormodel_hashtags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authormodel",
            name="hashtags",
            field=models.ManyToManyField(null=True, to="books.socialmediahandlemodel"),
        ),
    ]