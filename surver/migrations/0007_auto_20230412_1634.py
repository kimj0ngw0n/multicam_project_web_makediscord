# Generated by Django 3.2.18 on 2023-04-12 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surver', '0006_surver_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='surver.channel'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
