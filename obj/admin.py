from django.contrib import admin
from obj.models import *
from .views import *


class Cars(admin.ModelAdmin):
    list_display = ('id','placa','km_atual','estado_combustivel')

class Tyres(admin.ModelAdmin):
    list_display = ('id','__str__' ,'est_pneu')

class Travels(admin.ModelAdmin):
    list_display = ('veiculo', 'km_final','est_pne')


admin.site.register(Car,Cars)
admin.site.register(Tyre, Tyres)
admin.site.register(Modelo)
admin.site.register(Viajem, Travels)