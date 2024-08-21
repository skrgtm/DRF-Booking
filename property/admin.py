from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = Property.images.through
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'bhk_type', 'cost', 'created_at', 'updated_at')
    search_fields = ('title', 'property_type', 'bhk_type')
    list_filter = ('property_type', 'bhk_type', 'created_at')
    inlines = [PropertyImageInline]

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
