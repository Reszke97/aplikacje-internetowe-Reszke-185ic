# Generated by Django 3.1.3 on 2020-11-09 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201109_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='data_opublikowania',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='data_utworzenia',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='tekst',
        ),
    ]