from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name_cat = models.CharField(max_length=150, verbose_name="наименование категории")
    description_cat = models.TextField(**NULLABLE, verbose_name="описание")

    def __str__(self):
        return f'{self.name_cat}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name_prod = models.CharField(max_length=150, verbose_name="наименование продукта")
    description_prod = models.TextField(**NULLABLE, verbose_name="описание")
    image = models.ImageField(upload_to='product/', verbose_name="превью", **NULLABLE)
    purchase_price = models.IntegerField(verbose_name="цена за покупку")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")

    def __str__(self):
        return f'{self.name_prod} {self.category} {self.description_prod}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Version(models.Model):
    product = models.ForeignKey(Product, related_name="version", on_delete=models.CASCADE, verbose_name="продукт")
    version_number = models.IntegerField(verbose_name="номер версии")
    version_name = models.CharField(max_length=100, verbose_name="название версии")
    indicates_current_version = models.BooleanField(default=True, verbose_name="признак текущей версии")

    def __str__(self):
        return f'{self.product} {self.version_number} {self.version_name}'

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"


class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)
    content = models.TextField(**NULLABLE, verbose_name="контент")
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='превью')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return f'{self.heading}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
