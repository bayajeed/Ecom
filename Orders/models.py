from django.db import models

# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Orders.Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
    unit = models.CharField(max_length = 255, default = 'pcs')

    def __str__(self):
        return f' {self.cart.id} -> {self.product} -> {self.quantity}'
    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

class Cart(models.Model):
    user = models.OneToOneField('Users.CustomUser', on_delete=models.CASCADE)
    products = models.ManyToManyField('Products.Product', through = CartItem) 
    
    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'