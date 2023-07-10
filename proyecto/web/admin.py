from django.contrib import admin
from .models import Auto, Cliente, Producto, ImagenAuto

#subir mas de una imagen
class ImagenAutoAdmin(admin.TabularInline):
    model = ImagenAuto


    
class AutoAdmin(admin.ModelAdmin):
    list_display = ["marca","modelo","anno","precio"]
    list_editable = []
    search_fields = ["marca"]
    list_filter = ["anno"]
    list_per_page = 4
    inlines = [
        ImagenAutoAdmin
    ]
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre","appaterno","run"]
    list_editable = []
    search_fields = ["nombre"]
    list_filter = ["run"]
    list_per_page = 4
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","fecha_creacion"]
    search_fields = ["nombre"]
    list_filter = ["marca"]
    list_per_page = 4

admin.site.register(Auto, AutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)

# Register your models here.
