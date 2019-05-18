from django.contrib import admin
from .models import User


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['pr_id', 'email']
