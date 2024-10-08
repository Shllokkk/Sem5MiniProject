# Generated by Django 5.0.2 on 2024-04-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='desc',
        ),
        migrations.AddField(
            model_name='signup',
            name='Branch',
            field=models.CharField(default='IT', max_length=20),
        ),
        migrations.AddField(
            model_name='signup',
            name='Year',
            field=models.CharField(default='2', max_length=10),
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='123', max_length=15),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='sample@gmail.com', max_length=20),
        ),
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(default='xyz', max_length=30),
        ),
    ]
