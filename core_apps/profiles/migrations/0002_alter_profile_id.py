# Generated by Django 4.1.6 on 2023-02-15 22:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4b243469-db54-4574-90ef-83267abea6bd'), editable=False, unique=True),
        ),
    ]
