# Generated by Django 3.1.3 on 2022-04-10 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listazadan', '0003_auto_20220410_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zadanie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zadanie', to=settings.AUTH_USER_MODEL),
        ),
    ]
