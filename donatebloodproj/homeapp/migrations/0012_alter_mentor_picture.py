# Generated by Django 3.2.5 on 2022-03-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_auto_20220326_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='mentors/'),
        ),
    ]