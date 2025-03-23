from django.db import models


# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name_category}: {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name_category']


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение продукта', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория продукта', related_name="product", null=True)
    price = models.IntegerField(verbose_name='Цена продукта')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name_product} - {self.category}. Описание: {self.description}. Цена: {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name_product']


