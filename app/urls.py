from django.contrib import admin
from django.urls import path
from views import DashboardOperacao, RegistroUsuario

#path('app_principal/', include('app_principal.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registroUsuario/', RegistroUsuario.as_view(), name='registroUsuario'),
    path('usuarios/<int:usuario_id>/operacoes/', DashboardOperacao.as_view(), name='dashboard-operacoes'),
]
   
