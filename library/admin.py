from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'total_copies', 'available_copies', 'published_date')


admin.site.register(Book, BookAdmin)
