# Generated by Django 4.1.7 on 2023-03-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_buying_is_paid_buying_being_delivered_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buying',
            name='being_delivered',
        ),
        migrations.RemoveField(
            model_name='buying',
            name='is_delivered',
        ),
        migrations.AddField(
            model_name='buying',
            name='status',
            field=models.CharField(default='requested', max_length=20),
        ),
    ]
