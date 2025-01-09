from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, default="Uncategorized")
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

class Review(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.review_text} - {self.rating}'
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

# products review
#     user
#     product
#     review
#     //rating
#     date
#     status

# all reviews
# individual reviews