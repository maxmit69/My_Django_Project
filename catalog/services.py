from catalog.models import Category
from django.conf import settings
from django.core.cache import cache


def get_categories():
    """Возвращает все категории"""
    if not settings.CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
