# Generated by Django 2.2.1 on 2019-05-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_user_pr_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_id', models.IntegerField(unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='pr_id',
        ),
    ]
