# Generated by Django 3.0.5 on 2020-05-24 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_userprofile'),
        ('payments', '0004_order_successful'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='userprofile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.UserProfile'),
        ),
    ]
