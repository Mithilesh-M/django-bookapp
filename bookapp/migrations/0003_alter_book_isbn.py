# Generated by Django 3.2 on 2021-04-22 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
