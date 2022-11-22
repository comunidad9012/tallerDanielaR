from unicodedata import name
from django.urls import path, include
from . import views

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('', views.logout_view, name='logout'),
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('motos', views.motos, name='motos'),
    path('motos/busqueda', views.buscar, name='buscador'),
    path('motos/crear', views.crear, name='crear'),
    path('motos/editar', views.editar, name='editar'),
    path('motos/detalles', views.detalles, name='detalles'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('motos/editar/<int:id>', views.editar, name='editar'),
    path('motos/detalles/<int:id>', views.detalles, name='detalles'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/', views.salir, name='salir'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
