# Generated by Django 4.0 on 2021-12-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_phone_number_contact_home_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='home_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
