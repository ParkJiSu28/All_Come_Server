# Generated by Django 2.2.1 on 2019-05-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
