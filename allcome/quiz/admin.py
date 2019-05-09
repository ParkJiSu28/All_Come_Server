from django.contrib import admin
from .models import QuizModel


# Register your models here.
@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ['pr_id', 'subject', 'title']
    search_fields = ('pr_id', 'subject',)
