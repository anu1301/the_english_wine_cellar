# Generated by Django 3.2 on 2023-02-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine_tasting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiences',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
