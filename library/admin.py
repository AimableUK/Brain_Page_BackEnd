from django.contrib import admin
from .models import Book, Student, User, Borrowing


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'total_copies', 'available_copies')
    

admin.site.register(Book, BookAdmin)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Borrowing)
