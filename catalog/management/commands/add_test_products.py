from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных, предварительно удаляя существующие данные'

    def handle(self, *args, **kwargs):
        # Удаляем все существующие продукты
        Product.objects.all().delete()
        self.stdout.write(self.style.WARNING('Все существующие продукты были удалены.'))

        # Определяем категории, если они еще не существуют
        electronics, created = Category.objects.get_or_create(name_category="Электроника", description="Устройства и гаджеты")
        clothing, created = Category.objects.get_or_create(name_category="Одежда", description="Одежда и аксессуары")
        books, created = Category.objects.get_or_create(name_category="Books", description="Различные жанры книг")

        # Список тестовых продуктов
        products = [
            {
                "name_product": "Смартфон",
                "description": "Последняя модель смартфона",
                "image": " ",
                "category": electronics,
                "price": 699,
                "created_at": "2025-03-22",
                "updated_at": "2025-03-22T15:12:00.961Z"
            },
            {
                "name_product": "Футболка",
                "description": "Хлопковая футболка",
                "image": "",
                "category": clothing,
                "price": 19,
                "created_at": "2025-03-22",
                "updated_at": "2025-03-22T15:12:00.961Z"
            },
            {
                "name_product": "Роман",
                "description": "Художественная литература",
                "image": "",
                "category": books,
                "price": 9,
                "created_at": "2025-03-22",
                "updated_at": "2025-03-22T15:04:21.156Z"
            }
        ]

        # Добавляем тестовые продукты в базу данных
        for product_data in products:
            product, created = Product.objects.get_or_create(
                name_product=product_data["name_product"],
                defaults={
                    "description": product_data["description"],
                    "image": product_data["image"],
                    "category": product_data["category"],
                    "price": product_data["price"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт "{product.name_product}" был успешно добавлен.'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт "{product.name_product}" уже существует.'))

        self.stdout.write(self.style.SUCCESS('Все тестовые продукты обработаны.'))
