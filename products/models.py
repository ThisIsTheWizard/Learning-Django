from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=99, null=False, blank=False)
    img = models.ImageField(upload_to='assets/img/uploads/')
    desc = models.TextField(null=False, blank=False)
    old_price = models.DecimalField(decimal_places=2, max_digits=100, null=False, blank=False)
    new_price = models.DecimalField(decimal_places=2, max_digits=100, null=False, blank=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
