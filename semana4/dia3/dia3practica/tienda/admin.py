from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Cliente

admin.site.register(Categoria)
# admin.site.register(Producto)

# decorador https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # establezco q quiero q se vea
    list_display = ('pk','nombre','categoria','precio','stock')
    # para clickear y editar
    list_display_links = ('pk','nombre')
    list_editable = ('categoria','precio','stock')
    search_fields = ['nombre']
    
admin.site.register(Cliente)