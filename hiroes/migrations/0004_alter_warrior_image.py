# Generated by Django 5.1.1 on 2024-10-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hiroes", "0003_warrior_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="warrior",
            name="image",
            field=models.ImageField(default="بدون تصویر", upload_to="images"),
        ),
    ]
