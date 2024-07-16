from django.conf import settings
from django.core.cache import cache

from project.models import Product, Category


def get_category_from_cache():
    if not settings.CACHE_ENABLED:
        return Category.objects.all()
    key = 'proudcts_list'
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)
    return category