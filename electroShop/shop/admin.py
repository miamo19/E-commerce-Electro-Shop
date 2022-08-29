from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.
admin.site.site_header = "E-Commerce"
admin.site.site_title = "Electro-Shop"
admin.site.index_title = "Manager"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    
class AdminProducts(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price', 'category')

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'date_commande', 'total')
     

admin.site.register(Category, AdminCategorie)
admin.site.register(Product, AdminProducts)
admin.site.register(Commande, AdminCommande)