# Generated by Django 3.2.5 on 2022-03-22 12:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_donor_sub_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='suruKotha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]
