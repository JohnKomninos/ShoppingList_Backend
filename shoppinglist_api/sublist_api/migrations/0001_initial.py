# Generated by Django 4.0.5 on 2022-06-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sublist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('aisle', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
