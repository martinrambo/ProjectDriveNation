from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.inicio, name='index'),
    path('Catalogo', views.Catalogo, name='Catalogo'),
    path('Noticias', views.Noticias, name='Noticias'),
    path('Registro', views.Registro, name='Registro'),
    path('auto/<int:pk>/', views.car_detail, name='car_detail'),
    path('agregar-producto/', views.agregar_producto, name="agregar_producto"),
    path('listar-productos/', views.listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', views.modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('registro/', views.registro, name="registro"),
    path('Accesorios/', views.Accesorios, name="Accesorios"),
    path('agregar-auto/', views.agregar_auto, name="agregar_auto"),
    path('listar-autos/', views.listar_autos, name="listar_autos"),
    path('modificar-auto/<id>/', views.modificar_auto, name="modificar_auto"),
    path('eliminar-auto/<id>/', views.eliminar_auto, name="eliminar_auto"),
    path('detalle-auto/<int:auto_id>/', views.detalle_auto, name='detalle_auto'),
    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)