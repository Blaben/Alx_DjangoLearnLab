from django.contrib import admin
from .models import Author, Book, UserProfile, library

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(library)