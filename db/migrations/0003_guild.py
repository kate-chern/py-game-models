# Generated by Django 4.0.2 on 2024-01-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]