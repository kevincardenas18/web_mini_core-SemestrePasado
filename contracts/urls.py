from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('reporte/', views.report, name='reporte'),
    path('clientes/', views.client_list, name='clientes'),
    path('contratos/', views.contract_list, name='contratos'),
    path('', RedirectView.as_view(url='reporte/'), name='index'),
]