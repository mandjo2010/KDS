from distutils.command.upload import upload
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from utilisateurs.models import User
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.

CHOIX_STATUS = (
        ("traitement", "Traitement"),
        ("expédié", "Expédié"),
        ("livré", "Livré"),
)

STATUS = (
        ("en_attente", "En Attente"),
        ("en_cours", "En Cours"),
        ("publier", "Publier"),
        ("rejeté", "Rejeté"),
        ("désactivé", "Désactivé"),
)

NOTE = (
        (1, "✨☆☆☆☆"),
        (2, "✨✨☆☆☆"),
        (3, "✨✨✨☆☆"),
        (4, "✨✨✨✨☆"),
        (5, "✨✨✨✨✨"),
)


def user_directory_path(instance, filename):
        return 'user_{0}/{0}'.format(instance.user.id,  filename)


class Collection(models.Model):
        titre = models.CharField(max_length=100, default="model")
        slug = AutoSlugField(populate_from='titre', unique=True, null=True, default=None)
        image = models.ImageField(upload_to="collection",  help_text="Taille: 1024 x 1024", default="collection.jpg")

        class Meta:
                verbose_name_plural = "Collections"

        def collection_image(self):
                return mark_safe('<img src="%s" width="50" height="50" /> ' % (self.image.url))

        def __str__(self):
                return self.titre

        def get_absolute_url(self):
                return reverse('cœur:product_list_by_collection', args=[self.slug])


class Category(models.Model):
        titre = models.CharField(max_length=100, default="model")
        collection = models.ForeignKey(Collection, on_delete=models.SET_NULL,  null=True)
        slug = AutoSlugField(populate_from='titre', unique=True, null=True, default=None)
        image = models.ImageField(upload_to="category",  help_text="Taille: 1024 x 1024", default="")

        class Meta:
                ordering = ['titre']
                indexes = [
                        models.Index(fields=['titre']),
                ]
                verbose_name_plural = "Categories"
                verbose_name = 'category'

        def __str__(self):
                return self.titre

        def category_image(self):
                return mark_safe('<img src="%s" width="50" height="50" /> ' % (self.image.url))

        def get_absolute_url(self):
                return reverse('cœur:product_list_by_category', args=[self.slug])


class Tags(models.Model):
        pass


class Vendor(models.Model):
        titre = models.CharField(max_length=100, default="Paul")
        image = models.ImageField(upload_to="fournisseurs", default="")
        description = models.TextField(null=True, blank=True, default="je suis un fournisseur")
        adresse = models.CharField(max_length=100, default="1 Rue du fournisseur ")
        contact = models.CharField(max_length=100, default="+33 7 64 45 02 23 ")
        temps_chat = models.CharField(max_length=100, default="100")
        durée_de_livraison = models.CharField(max_length=100, default="100")
        évaluation_authentiques = models.CharField(max_length=100, default="100")
        retour_sous_30_jours = models.CharField(max_length=100, default="100")
        période_de_garantie = models.CharField(max_length=100, default="100")

        user = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True)

        class Meta:
                verbose_name_plural = "Fournisseurs"

        def vendor_image(self):
                return mark_safe('<img src="%s" width="50" height="50" /> ' % (self.image.url))

        def __str__(self):
                return self.titre


class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True)
        category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True, )
        titre = models.CharField(max_length=100, default="t-shirt")
        slug = AutoSlugField(populate_from='titre', unique=True, null=True, default=None)
        image = models.ImageField(upload_to="produits/%Y/%m/%d", help_text="Taille: 1024 x 1024", default="")
        image_view = models.ImageField(upload_to="produits/%Y/%m/%d", help_text="Taille: 1024 x 1024", default="")
        image_sm_1 = models.ImageField(upload_to="produit-single1/%Y/%m/%d", help_text="Taille: 1488 x 1488", default="")
        image_sm_2 = models.ImageField(upload_to="produit-single2/%Y/%m/%d", help_text="Taille: 1488 x 1488", default="")
        image_sm_3 = models.ImageField(upload_to="produit-single3/%Y/%m/%d", help_text="Taille: 1488 x 1488", default="")
        description = models.TextField(null=True, blank=True, default="c'est un produit")
        price = models.DecimalField(max_digits=12, decimal_places=2,  default="1.99")
        prix_ancien = models.DecimalField(max_digits=12, decimal_places=2, default="2.99")
        specificationns = models.TextField(null=True, blank=True)
        statut_produit = models.CharField(choices=STATUS, max_length=100, default="en_cours")
        status = models.BooleanField(default="True")
        en_stock = models.BooleanField(default="True",)
        featured = models.BooleanField(default="False")
        digital = models.BooleanField(default="False")
        ref = ShortUUIDField(unique=True, length=4, max_length=10, prefix="ref", alphabet="1234567890")
        date = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(null=True, blank=True)

        class Meta:
                ordering = ['titre']
                indexes = [
                        models.Index(fields=['id', 'slug']),
                        models.Index(fields=['titre']),
                        models.Index(fields=['-date']),
                ]
                verbose_name_plural = "Produits"

        def __str__(self):
                return self.titre

        def product_image(self):
                return mark_safe('<img src="%s" width="50" height="50" /> ' % (self.image.url))

        def get_percentage(self):
                nouveau_prix = (self.price / self.prix_ancien) * 100
                return nouveau_prix

        def get_absolute_url(self):
                return reverse('cœur:product_detail', args=[self.id, self.slug])




class ProductImages(models.Model):
        images = models.ImageField(upload_to="product-images",  default="")
        produit = models.ForeignKey(Product, on_delete=models.SET_NULL,  null=True)
        date = models.DateTimeField(auto_now_add=True)

        class Meta:
                verbose_name_plural = "Images Produits"


############################ Panier ###################
class CartOrder(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=12, decimal_places=2, default="1.99")
        suivi_paiement = models.BooleanField(default="False")
        date_commande = models.DateTimeField(auto_now_add=True)
        statut_produit = models.CharField(choices=CHOIX_STATUS, max_length=100, default="traitement")

        class Meta:
                verbose_name_plural = "Mon Panier "

############################ ArticlesCommandes ###################


class CartOrderItems(models.Model):
        commande = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
        numéro_facture = models.CharField(max_length=200,)
        statut_produit = models.CharField(max_length=200,)
        article = models.CharField(max_length=200,)
        image = models.CharField(max_length=200,)
        quantité = models.IntegerField(default=0,)
        price = models.DecimalField(max_digits=12, decimal_places=2,  default="1.99")
        total = models.DecimalField(max_digits=12, decimal_places=2,  default="1.99")

        class Meta:
                verbose_name_plural = "Articles de Mon Panier "

        def order_img(self):
                return mark_safe('<img src="/media/%s" width="50" height="50" /> ' % (self.image))

############################ Product Review ###################


class ProductReview(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        produit = models.ForeignKey(Product, on_delete=models.CASCADE)
        avis = models.TextField()
        note = models.IntegerField(choices=NOTE, default=None)
        date = models.DateTimeField(auto_now_add=True)

        class Meta:
                verbose_name_plural = "Évaluations d'utilisateurs"

        def __str__(self):
                return self.product.titre

        def get_rating(self):
                return self.avis

############################ Liste d'envies ###################


class wishlist(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        produit = models.ForeignKey(Product, on_delete=models.CASCADE)
        date = models.DateTimeField(auto_now_add=True)

        class Meta:
                verbose_name_plural = "Ma liste d'envies"

        def __str__(self):
                return self.product.titre

############################ Adresses ###################


class Adresse(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        adresse = models.CharField(max_length=100, null=True)
        status = models.BooleanField(default="False")

        class Meta:
                verbose_name_plural = "Adresse"
