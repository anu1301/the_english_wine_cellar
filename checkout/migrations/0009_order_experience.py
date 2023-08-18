# Generated by Django 3.2 on 2023-08-17 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine_tasting', '0003_alter_experiences_image'),
        ('checkout', '0008_orderlineitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine_tasting.experiences'),
        ),
    ]