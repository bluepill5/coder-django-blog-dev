# Generated by Django 3.2.9 on 2022-01-16 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_rename_blogs_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='fecha_inscripcion',
            new_name='date_creation',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='fecha_inscripcion',
            new_name='date_subscription',
        ),
    ]
