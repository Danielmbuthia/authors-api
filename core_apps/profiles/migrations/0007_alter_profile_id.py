# Generated by Django 4.1.6 on 2023-02-22 00:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bb288ae1-6001-4f7b-b53a-c1553388ada7'), editable=False, unique=True),
        ),
    ]
