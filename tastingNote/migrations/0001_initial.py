# Generated by Django 4.0.6 on 2022-08-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagemeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='datatime')),
                ('image_file_name', models.CharField(db_column='image_file_name', max_length=200)),
            ],
        ),
    ]