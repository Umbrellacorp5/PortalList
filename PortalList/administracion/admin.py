# Register your models here.
#añadir apps al panel de admin
#como se vera el admin de djago
from django.contrib import admin

from .models import Administrador, Pasan, Grupo

admin.site.register(Administrador)
admin.site.register(Pasan)
admin.site.register(Grupo)