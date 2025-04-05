from django.contrib import admin

from .models import Category, Foods, Comment

admin.site.register(Category)
admin.site.register(Foods)
admin.site.register(Comment)