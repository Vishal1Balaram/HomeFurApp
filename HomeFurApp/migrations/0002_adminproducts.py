# Generated by Django 5.0.2 on 2024-02-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeFurApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('condition', models.CharField(max_length=100)),
                ('noofdays', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=200)),
                ('options', models.CharField(max_length=500)),
                ('rentaloptions', models.CharField(max_length=500)),
            ],
        ),
    ]