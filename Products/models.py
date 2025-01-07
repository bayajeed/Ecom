from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'category_images/', blank= True, null = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'product_images/', blank= True, null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank = True)
    base_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    in_stock = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

# products review
#     user
#     product
#     review
#     //rating
#     date
#     status

# all reviews
# individual reviews