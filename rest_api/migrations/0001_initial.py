# Generated by Django 2.1.1 on 2018-09-09 15:38

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
