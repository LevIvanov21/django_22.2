from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_to_buy = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True)
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}: ({self.description}; {self.created_at}; {self.updated_at}; {self.owner})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

        permissions = [
            (
                'edit_publication',
                'изменить публикацию'
            ),
            (
                'edit_description',
                'изменить описание'
            ),
            (
                'edit_categories',
                'изменить категорию'
            ),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='Версия продукта')
    name_of_version = models.CharField(max_length=150, verbose_name='Название версии')
    actual_version_indicator = models.BooleanField(default=True, verbose_name='Актуальная версия')

    def __str__(self):
        return f'{self.name_of_version}: {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'