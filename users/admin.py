from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
     'get_avatar', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login')

    def get_avatar(self, object):
        """ Выводит изображение в админке """
        if object.avatar:
            return mark_safe(f'<img src="{object.avatar.url}" width="70" height="50" />')

    get_avatar.short_description = 'Аватар'

