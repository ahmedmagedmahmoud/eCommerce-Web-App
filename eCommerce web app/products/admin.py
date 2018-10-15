from django.contrib import admin

from .models import Product, ProductFile


class ProductFileInline(admin.TabularInline):
    model = ProductFile
    extra = 1  # by default there will be only one file 


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'is_digital']
    inlines = [ProductFileInline]  # the inline only works if only ther e was a foreignkey
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
