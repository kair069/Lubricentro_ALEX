from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('cargar_excel/', views.cargar_datos_excel, name='cargar_excel'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),    
    path('productos/actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/detalle/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('calcular-costo/', views.calcular_costo, name='calcular_costo'),
    path('estadisticas/costos/', views.analisis_costos, name='analisis_costos'),
    path('estadisticas/estadisticas_inventario/', views.estadisticas_inventario, name='estadisticas_inventario'),
    path('crear-marca/', views.crear_marca, name='crear_marca'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('ventas-por-marca/', views.ventas_por_marca_view, name='ventas_por_marca'),
    # path('distribucion-categoria/', views.categoria_distribution_view, name='distribucion_categoria'),
    # path('tendencia-stock/', views.stock_trend_view, name='tendencia_stock'),

]
