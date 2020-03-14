from django.contrib import admin

from .models import Gerente, Cliente, Produto, Vendedor, Tecnico

admin.site.register(Gerente)
admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Vendedor)
admin.site.register(Produto)

# Register your models here.
