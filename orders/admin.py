from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemInline(admin.TabularInline):
        model = OrderItem
        raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
        list_display = ['id', 'prénom', 'nom', 'email', 'adresse', 'code_postal', 'ville', 'payé', 'date', 'updated']
        list_filter = ['payé', 'date', 'updated']
        inlines = [OrderItemInline]
