from django.core.management import BaseCommand
import json

from django.db import connection

from project.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog/fixtures/category_data.json', 'r', encoding='UTF-8') as category_file:
            data = json.load(category_file)
        return data

    @staticmethod
    def json_read_products():
        with open('catalog/fixtures/product_data.json', 'r', encoding='UTF-8') as product_file:
            data = json.load(product_file)
        return data

    def handle(self, *args, **options):

        with connection.cursor() as cur:
            cur.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price_to_buy=product['fields']['price_to_buy'])
            )

        Product.objects.bulk_create(product_for_create)