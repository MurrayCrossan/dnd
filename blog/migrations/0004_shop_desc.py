# Generated by Django 4.0.3 on 2022-03-10 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_shop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]