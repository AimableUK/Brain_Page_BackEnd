from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


class AccountAdmin(UserAdmin):
    list_display = ('username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('username',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    # @admin.display(description="Profile Picture")
    # def thumbnail(self, object):
    #     return format_html(
    #         '<img src="{}" width="30" style="border-radius:50%;" />',
    #         object.profile_picture.url
    #     )
        
    # # use decorator instead of this -> thumbnail.short_description = 'Profile Picture' 
    # list_display = ('thumbnail', 'member')
    pass
    

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile)
