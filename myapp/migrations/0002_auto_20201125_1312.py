# Generated by Django 3.1.3 on 2020-11-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalrecord',
            name='method',
            field=models.TextField(max_length=300),
        ),
    ]