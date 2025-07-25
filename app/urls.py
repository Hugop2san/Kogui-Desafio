from django.contrib import admin
from django.urls import path
from .views import RegistroUsuario, DashboardOperacao, DetalheUsuario

urlpatterns = [
    path('registro/', RegistroUsuario.as_view() , name='registro-usuario'),
    path('usuarios/<int:usuario_id>/operacoes/', DashboardOperacao.as_view(), name='dashboard-operacoes'),
    path('usuarios/<int:pk>/', DetalheUsuario.as_view(), name='detalhe-usuario')
]
