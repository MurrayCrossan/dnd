# Generated by Django 4.0.3 on 2022-03-11 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_continent_tag_item_effect_nation_tag_person_context_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='tag',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
    ]
