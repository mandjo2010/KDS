from django.contrib import admin
from cœur.models import Product, CartOrder, Category, Collection, Vendor, ProductImages, wishlist, Adresse, ProductReview, CartOrderItems


# Register your models here.
class ProductImagesAdmin(admin.TabularInline):
        model = ProductImages

class ProductAdmin(admin.ModelAdmin):
        inlines = [ProductImagesAdmin]
        list_display = ['user', 'titre', 'product_image', 'price', 'featured', 'statut_produit']
        list_filter = ['featured', 'date', 'updated']
        list_editable = ['price', 'featured']



class CategoryAdmin(admin.ModelAdmin):
        list_display = ['titre', 'category_image', ]


class CollectionAdmin(admin.ModelAdmin):
        list_display = ['titre', 'collection_image', ]


class VendorAdmin(admin.ModelAdmin):
        list_display = ['vendor_image', 'titre',]


class CartOrderAdmin(admin.ModelAdmin):
        list_idsplay = ['user', 'price', 'suivi_paiement','date_commande', 'statut_produit',]


class CartOrderItemsAdmin(admin.ModelAdmin):
        list_idsplay = ['commande', 'price', 'numéro_facture','article',  'image', 'quantité',  'total']


class ProductReviewAdmin(admin.ModelAdmin):
        list_display = ['user', 'produit', 'avis', 'note', 'date',]


class wishlistAdmin(admin.ModelAdmin):
        list_display = ['user', 'produit', 'date',]


class AdresseAdmin(admin.ModelAdmin):
        list_display = ['user', 'adresse', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist, wishlistAdmin)
admin.site.register(Adresse, AdresseAdmin)
