# Generated by Django 2.2.2 on 2019-06-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0003_auto_20190615_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='<...To be set later...>', max_length=100),
        ),
    ]