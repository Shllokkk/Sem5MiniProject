# Generated by Django 5.0.2 on 2024-04-15 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_querry_cat_alter_signup_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querry',
            old_name='cat',
            new_name='Cat',
        ),
        migrations.RemoveField(
            model_name='querry',
            name='id',
        ),
        migrations.AddField(
            model_name='querry',
            name='query_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='querry',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='querry',
            name='email',
            field=models.EmailField(max_length=122),
        ),
    ]
