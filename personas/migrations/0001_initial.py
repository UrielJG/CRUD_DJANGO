# Generated by Django 4.1.4 on 2022-12-15 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nacionalidad', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
