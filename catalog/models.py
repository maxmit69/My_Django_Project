from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name_prod = models.CharField(max_length=150, verbose_name="наименование продукта")
    description_prod = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to='product/', verbose_name="превью", **NULLABLE)
    purchase_price = models.IntegerField(verbose_name="цена за покупку")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="категория")

    def __str__(self):
        return f'{self.name_prod} {self.category} {self.description_prod}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Category(models.Model):
    name_cat = models.CharField(max_length=150, verbose_name="наименование категории")
    description_cat = models.TextField(verbose_name="описание")

    def __str__(self):
        return f'{self.name_cat}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
