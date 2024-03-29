from django.contrib import admin
from cars.models import Car, Brand

# contém todas as configurações  da seção carros no painel do admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

#registra a seção
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
