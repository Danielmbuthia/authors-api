# Generated by Django 4.1.6 on 2023-02-22 00:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2fe3aacc-94c1-4521-9116-4b654e830a34'), editable=False, unique=True),
        ),
    ]
