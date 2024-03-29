from django.contrib import admin
from .models import Portafolio

class PortafolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Portafolio, PortafolioAdmin)