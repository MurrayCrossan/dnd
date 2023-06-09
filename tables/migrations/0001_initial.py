# Generated by Django 4.0.3 on 2022-03-27 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snip', models.CharField(max_length=200)),
                ('entry', models.TextField()),
                ('cr', models.CharField(max_length=20)),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.table')),
            ],
        ),
    ]
