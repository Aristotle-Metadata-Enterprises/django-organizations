# Generated by Django 4.0.7 on 2022-10-13 02:45

from django.db import migrations
import organizations.fields


class Migration(migrations.Migration):

    dependencies = [
        ('test_abstract', '0003_alter_custominvitation_invited_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorganization',
            name='slug',
            field=organizations.fields.SlugField(blank=True, editable=False, help_text='The name in all lowercase, suitable for URL identification', max_length=200, populate_from='name', unique=True),
        ),
    ]