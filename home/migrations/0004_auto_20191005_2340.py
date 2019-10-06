# Generated by Django 2.2.6 on 2019-10-05 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='angry_index',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='bored_index',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='exited_index',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='fear_index',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sad_index',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]