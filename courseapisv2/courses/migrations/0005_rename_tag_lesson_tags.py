# Generated by Django 5.1.2 on 2024-11-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag_lesson_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='tag',
            new_name='tags',
        ),
    ]
