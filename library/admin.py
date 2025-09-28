from django.contrib import admin
from .models import Book, Student, User, Borrowing

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Borrowing)
