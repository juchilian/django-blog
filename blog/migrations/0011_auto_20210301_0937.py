# Generated by Django 2.2 on 2021-03-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210224_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]