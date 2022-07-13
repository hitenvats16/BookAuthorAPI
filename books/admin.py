from django.contrib import admin

from .models import Book

# Registering Book model to admin

admin.site.register(Book)
