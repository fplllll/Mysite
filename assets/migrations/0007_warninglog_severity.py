# Generated by Django 2.1.3 on 2018-12-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_warninglog'),
    ]

    operations = [
        migrations.AddField(
            model_name='warninglog',
            name='severity',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Slight'), (1, 'Attention'), (2, 'Serious')], null=True, verbose_name='Warning severity'),
        ),
    ]
