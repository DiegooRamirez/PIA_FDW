from django.contrib import admin
from .models import Auto, Sucursal, Producto, Evento, Opinion, Contacto

admin.site.register(Auto)
admin.site.register(Sucursal)
admin.site.register(Producto)
admin.site.register(Evento)
admin.site.register(Opinion)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha', 'leido')
    list_filter = ('leido', 'fecha')
    search_fields = ('nombre', 'email', 'asunto', 'mensaje')
    readonly_fields = ('fecha',)

