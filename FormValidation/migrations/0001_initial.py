# Generated by Django 3.2 on 2022-05-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.CharField(max_length=15)),
            ],
        ),
    ]
