from django.contrib import admin
from .models import produit

# admin.site.register(produit)
# Register your models here.
class produitAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')

admin.site.register(produit, produitAdmin)