from django.urls import path

from home.views import inicio_views, leer_datos, separa_styles, ver_styles

urlpatterns = [
    path('', inicio_views, name='home'),
    path('leer_datos', leer_datos, name='leer_datos'),
    path('separa_styles', separa_styles, name='separa_styles'),
    path('ver_styles', ver_styles, name='ver_styles'),

]