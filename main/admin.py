from django.contrib import admin
from main.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
    # list_display_links = None
    list_editable = ('description', 'price')


admin.site.register(Product, ProductAdmin)

