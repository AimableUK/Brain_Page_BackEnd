from django.contrib import admin
from .models import Book, Member, Lend

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'total_copies', 'available_copies', 'published_date')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'address', 'created_at')


class LendAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'lent_date', 'return_date', 'returned_at')


admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Lend, LendAdmin)
