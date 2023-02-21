# Generated by Django 4.1.6 on 2023-02-21 20:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('19ba7516-fd6d-4722-ad39-a101b1d07846'), editable=False, unique=True),
        ),
    ]