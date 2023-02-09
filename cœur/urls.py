from django.urls import path
from cœur import views
from cœur.views import product_list

app_name = 'cœur'

urlpatterns = [
        path('', views.product_list, name='product_list'),
        path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
        path('<slug:collection_slug>/', views.category_list, name='category_list_by_collection'),
        path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]


