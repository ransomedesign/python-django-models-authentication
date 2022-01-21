# Generated by Django 2.2.9 on 2022-01-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('tags', models.ManyToManyField(related_name='posts', to='mainapp.Tag')),
            ],
        ),
    ]
