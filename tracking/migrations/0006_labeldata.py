# Generated by Django 3.2.7 on 2022-07-28 19:01

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_expressprioritytracking_expresswithsigprioritytracking_prioritywithsigtracking'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderData', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]
