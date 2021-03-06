# Generated by Django 4.0.3 on 2022-04-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='Naming')),
                ('anons', models.CharField(default='anons', max_length=250, verbose_name='Intro')),
                ('full_text', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(verbose_name='Publication date')),
            ],
        ),
    ]
