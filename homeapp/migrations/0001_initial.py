# Generated by Django 4.2.6 on 2023-10-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sjimg')),
                ('name', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('views', models.IntegerField()),
            ],
        ),
    ]