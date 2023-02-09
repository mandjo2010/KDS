from django.db import models
from cœur.models import Product

# Create your models here.
STATUT_DE_LA_COMMANDE = [
        ('commande_créée', 'Commande Créée'),
        ("en_attente", "En Attente"),
        ("en_cours_de_traitement", "En Cours De Traitement"),
        ('Commande_expédiée', 'Commande Expédiée'),
        ('Commande_livrée', 'Commande Livrée'),
        ('Completed', 'Completed')
]

class Order(models.Model):
        prénom = models.CharField(max_length=50)
        nom = models.CharField(max_length=50)
        email = models.EmailField()
        adresse = models.CharField(max_length=250)
        code_postal = models.CharField(max_length=20)
        ville = models.CharField(max_length=100)
        date = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        payé = models.BooleanField(default=False)
        status = models.CharField(max_length=30, choices=STATUT_DE_LA_COMMANDE, default='commande_créée')

        class Meta:
                ordering = ['-date']
                indexes = [
                        models.Index(fields=['-date']),
        ]
                verbose_name_plural = "Commandes"

        def __str__(self):
                return f'Order {self.id}'

        def get_total_cost(self):
                return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
        order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
        product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
                return str(self.id)

        def get_cost(self):
                return self.price * self.quantity
