# Generated by Django 2.2.2 on 2019-10-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='entry',
            field=models.TextField(max_length=300),
        ),
    ]
