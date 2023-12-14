# Generated by Django 4.1.7 on 2023-03-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.IntegerField()),
                ('student_id', models.TextField()),
                ('name', models.TextField()),
                ('status', models.IntegerField()),
                ('edu', models.TextField()),
                ('advisor', models.TextField()),
                ('work', models.TextField()),
                ('public', models.IntegerField()),
                ('journal', models.IntegerField()),
                ('implemment', models.TextField()),
                ('meeting', models.TextField()),
                ('from_date', models.TextField()),
                ('to_date', models.TextField()),
                ('year', models.TextField()),
            ],
        ),
    ]
