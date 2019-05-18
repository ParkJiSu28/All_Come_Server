# Generated by Django 2.2.1 on 2019-05-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='algorithme',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='computer_network',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='computer_structure',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_structure',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='database',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='operation_system',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='software_engineering',
            field=models.IntegerField(default='1'),
        ),
    ]