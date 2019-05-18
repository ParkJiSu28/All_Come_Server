from django.db import models
from register.models import User
from quiz.models import QuizModel


class Like(models.Model):
    email = models.ForeignKey(User, on_delete=None, related_name=None)
    pr_id = models.ForeignKey(QuizModel, on_delete=None, related_name=None)



