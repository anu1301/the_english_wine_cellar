# Generated by Django 3.2 on 2023-03-05 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230217_1221'),
        ('booking', '0002_auto_20230228_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='experience_choice',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='original_booking',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to='profiles.userprofile'),
        ),
    ]
