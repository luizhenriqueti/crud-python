from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('/', home),

    #PESSOAS
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('deletar/<int:id>', delete, name='deletar')

    #ENDEREÇOS

]