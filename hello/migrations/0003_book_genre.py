# Generated by Django 4.1.1 on 2023-07-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Kryminał'), (2, 'Horror'), (3, 'Fantasy'), (4, 'Romans')], default=1),
        ),
    ]
