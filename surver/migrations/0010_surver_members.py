# Generated by Django 3.2.18 on 2023-04-12 22:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surver', '0009_alter_access_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='surver',
            name='members',
            field=models.ManyToManyField(through='surver.Access', to=settings.AUTH_USER_MODEL),
        ),
    ]
