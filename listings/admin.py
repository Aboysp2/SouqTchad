from django.contrib import admin
from .models import Category, Listing

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'seller', 'city', 'created_at', 'is_active')
    list_filter = ('category', 'city', 'is_active')
    search_fields = ('title', 'description')
