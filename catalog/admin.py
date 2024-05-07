from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_prod', 'purchase_price', 'category', 'description_prod', 'user')
    list_filter = ('category',)
    search_fields = ('name_prod', 'description_prod')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'is_published', 'date_created', 'views_count',)
    list_filter = ('is_published',)
    search_fields = ('heading',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'indicates_current_version',)
    list_filter = ('product',)
