# Generated by Django 5.0.2 on 2024-04-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_signup_desc_signup_branch_signup_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='querry',
            name='cat',
            field=models.CharField(default='Other', max_length=20),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='sample@gmail.com', max_length=40),
        ),
    ]
