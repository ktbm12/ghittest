from django.urls import path
from .views import index, Create_Produit
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Page de connexion
    path('login/', views.login_view, name='login'),
    
    
    # Page de déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('create-produit/', Create_Produit.as_view(), name='create'),
     path('produit/delete/<int:pk>/', views.delete_produit, name='delete_produit'),
       path('produit/update/<int:pk>/', views.update_produit, name='update_produit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    