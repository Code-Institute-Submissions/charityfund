# Generated by Django 3.0.5 on 2020-04-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200413_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
