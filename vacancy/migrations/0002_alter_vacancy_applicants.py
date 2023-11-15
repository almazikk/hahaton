# Generated by Django 4.2.7 on 2023-11-14 14:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]
