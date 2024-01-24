# Generated by Django 4.0.2 on 2024-01-24 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_guild'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.guild')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race')),
            ],
        ),
    ]