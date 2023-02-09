from django.shortcuts import render,  get_object_or_404
from cœur.models import Product, CartOrder, Category, Collection, Vendor, ProductImages, wishlist, Adresse, ProductReview, CartOrderItems
from cart.forms import CartAddProductForm
# Create your views here.


def product_list(request, category_slug=None):
        # produits = Produit.objects.all().order_by("?")
        # produits = Produit.objects.filter(statut_produit="publier", featured=True)
        category = None
        categories = Category.objects.all()
        products =Product.objects.all().filter(en_stock=True)
        collections = Collection.objects.all()
        cart_product_form = CartAddProductForm()
        if category_slug :
                category = get_object_or_404(Category, slug=category_slug )
                products = products.filter(category=category)
                collections = Collection.objects.all()
                cart_product_form = CartAddProductForm()

        context = {
                'products': products,
                'categories': categories,
                'category': category,
                'collections': collections,
                'cart_product_form': cart_product_form
        }
        return render(request, 'produits/list.html', context)


def product_detail(request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug,  en_stock=True, featured=True)
        cart_product_form = CartAddProductForm()
        context = {
                'product': product,
                'cart_product_form': cart_product_form,
        }
        return render(request, 'produits/detail.html', context)


def category_list(request,  collection_slug=None):
        collection = None
        collections = Collection.objects.all()
        categories = Category.objects.all().filter(slug=collection_slug)

        if collection_slug:
                collection = get_object_or_404(Collection, slug=collection_slug)
                categories= categories.filter(collection=collection)

        context = {
                'collection': collection,
                'categories': categories,
                'collections': collections,

        }
        return render(request, 'partials/nav.html', context)

