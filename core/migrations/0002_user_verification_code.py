# Generated by Django 4.2.3 on 2023-08-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
