from django.contrib import admin
from django.utils.safestring import mark_safe

from catalog.models import Product, Category, Blog, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'name_prod', 'purchase_price', 'category', 'get_image', 'description_prod', 'user', 'is_published_prod',)
    list_filter = ('category',)
    search_fields = ('name_prod', 'description_prod',)

    def get_image(self, object):
        """ Выводит изображение в админке """
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="70" height="100" />')

    get_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'is_published', 'date_created', 'views_count',)
    list_filter = ('is_published',)
    search_fields = ('heading',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'indicates_current_version',)
    list_filter = ('product',)
