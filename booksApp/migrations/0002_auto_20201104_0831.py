# Generated by Django 3.1.2 on 2020-11-04 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'managed': True},
        ),
    ]
