from django.urls import path
from utilisateurs import views

app_name = "utilisateurs"

urlpatterns = [
        path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
]
