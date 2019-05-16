from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100,unique=True,null=False)
    algorithme = models.IntegerField(default='1')
    database = models.IntegerField(default='1')
    computer_network = models.IntegerField(default='1')
    computer_structure = models.IntegerField(default='1')
    data_structure = models.IntegerField(default='1')
    operation_system = models.IntegerField(default='1')
    software_engineering = models.IntegerField(default='1')

