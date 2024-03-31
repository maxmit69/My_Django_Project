import json

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('cat_data.json', encoding="UTF-8") as json_file:
            cat = json.load(json_file)
            return [item for item in cat if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        with open('prod_data.json', encoding="UTF-8") as json_file:
            prod = json.load(json_file)
            return [item for item in prod if item["model"] == "catalog.product"]

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category_item in Command.json_read_categories():
            category_for_create.append(
                Category(id=category_item['pk'],
                         name_cat=category_item['fields']['name_cat'],
                         description_cat=category_item['fields']['description_cat'],
                         ))

        Category.objects.bulk_create(category_for_create)

        for product_item in Command.json_read_products():
            product_for_create.append(
                Product(id=product_item['pk'],
                        name_prod=product_item['fields']['name_prod'],
                        image=product_item['fields']['image'],
                        description_prod=product_item['fields']['description_prod'],
                        purchase_price=product_item['fields']['purchase_price'],
                        category=Category.objects.get(pk=product_item['fields']['category'])

                        ))

        Product.objects.bulk_create(product_for_create)
