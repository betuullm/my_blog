# Generated by Django 3.2.25 on 2025-05-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Hakkımda', max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
