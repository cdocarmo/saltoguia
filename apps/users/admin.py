from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
from users.models import UserProfile


class UserAdmin(ModelAdmin):
    list_display = ('date', 'last_login', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('first_name', 'email')
    
site.register(UserProfile, UserAdmin)
