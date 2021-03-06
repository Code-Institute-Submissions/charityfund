# Generated by Django 3.0.5 on 2020-05-24 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_userprofile'),
        ('payments', '0005_order_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.UserProfile'),
        ),
    ]
