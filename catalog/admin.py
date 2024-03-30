from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_prod', 'purchase_price', 'category', 'description_prod')
    list_filter = ('category',)
    search_fields = ('name_prod', 'description_prod')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat')
