# Generated by Django 4.1.2 on 2022-10-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0002_alter_wallpaper_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wallpaper", old_name="title", new_name="imagNAME",
        ),
        migrations.AddField(
            model_name="wallpaper",
            name="imagSRC",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="wallpaper",
            name="imagTAGS",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
