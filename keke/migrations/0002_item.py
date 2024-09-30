# Generated by Django 5.1.1 on 2024-09-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
