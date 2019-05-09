from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.TextField()
    algorithme = models.IntegerField()
    database = models.IntegerField()
    computer_network = models.IntegerField()
    computer_structure = models.IntegerField()
    data_structure = models.IntegerField()
    operation_system = models.IntegerField()
    software_engineering = models.IntegerField()
