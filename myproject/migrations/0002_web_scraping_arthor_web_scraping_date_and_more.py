# Generated by Django 4.1 on 2022-08-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_scraping',
            name='arthor',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='web_scraping',
            name='date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='web_scraping',
            name='url',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='web_scraping',
            name='header',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
