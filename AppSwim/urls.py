from django.urls import path
from AppSwim.views import *

urlpatterns = [
    path('', inicio),
    path('inicio/', inicio),
    path('create_nadadores/', create_nadadores),
    path('read_nadadores/', read_nadadores),
    path('update_nadadores/<id_nadador>', update_nadadores),
    path('delete_nadadores/<id_nadador>', delete_nadadores),
    path('create_profesores/', create_profesores),
    path('read_profesores/', read_profesores),
    path('update_profesores/<id_profesor>', update_profesores),
    path('delete_profesores/<id_profesor>', delete_profesores),
    path('create_estilos/', create_estilos),
    path('read_estilos/', read_estilos),
    path('update_estilos/<id_estilo>', update_estilos),
    path('delete_estilos/<id_estilo>', delete_estilos),
    path('create_slots/', create_slots),
    path('read_slots/', read_slots),
    path('update_slots/<id_slot>', update_slots),
    path('delete_slots/<id_slot>', delete_slots),
    # path('pasadas/', pasadas),
    # path('series/', series),
    # path('sesiones/', sesiones),
    # path('niveles/', niveles),
    # path('carriles/', carriles),
    # path('cadencia/', cadencia),
]