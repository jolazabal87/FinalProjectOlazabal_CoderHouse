# Generated by Django 4.0.5 on 2022-07-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessApp', '0010_detail_ticket_ticketet_delete_ticket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_ticket',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
