from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    description = models.TextField(max_length=1200)
    image_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
