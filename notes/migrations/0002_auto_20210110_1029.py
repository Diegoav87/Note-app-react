# Generated by Django 3.1.5 on 2021-01-10 16:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
