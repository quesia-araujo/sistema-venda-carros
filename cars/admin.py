from django.contrib import admin
from cars.models import Car

# contém todas as configurações  da seção carros no painel do admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

#registra a seção
admin.site.register(Car, CarAdmin)