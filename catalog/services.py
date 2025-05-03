from django.core.cache import cache
from config.settings import CACHES_ENABLED
from .models import Product, Category


def get_products_by_category(category_id):
    """Возвращает QuerySet продуктов указанной категории"""
    return Product.objects.filter(category_id=category_id)

def get_products_from_cache():
    """Низкоуровневое кэширование продуктов"""

    if not CACHES_ENABLED:
        return Product.objects.all()

    key = "products_list"
    info_cache = cache.get(key)
    if info_cache is not None:
        return info_cache
    info_cache = Product.objects.all()
    cache.set(key, info_cache)
    return info_cache

def get_products_by_category_from_cache(category_id):
    """Возвращает кешированные продукты категории"""
    if not CACHES_ENABLED:
        return Product.objects.filter(category_id=category_id).select_related('category')

    key = f"products_category_{category_id}"
    products = cache.get(key)
    if products is None:
        products = Product.objects.filter(category_id=category_id).select_related('category')
        cache.set(key, products, timeout=60 * 15)  # Кеш на 15 минут
    return products