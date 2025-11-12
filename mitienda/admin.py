from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} #autocompleta el campo slug basado en el campo name

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('name',)}
