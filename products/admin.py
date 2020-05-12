from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['title', 'desc']
    list_display = ['title', 'old_price', 'new_price', 'created_at', 'updated_at', 'slug', 'active']
    list_editable = ['old_price', 'new_price', 'active']
    list_filter = ['old_price', 'new_price', 'active', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
