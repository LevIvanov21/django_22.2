from django.contrib import admin

from project.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_to_buy', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'name_of_version', 'actual_version_indicator',)
    list_filter = ('version_number', 'name_of_version',)
    search_fields = ('name_of_version',)
