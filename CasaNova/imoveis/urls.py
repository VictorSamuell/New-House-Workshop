from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ImovelListView, ImovelDetailView, ImovelCreateView,
    ImovelUpdateView, ImovelDeleteView, ImovelViewSet
)

router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet, basename='imovel')

urlpatterns = [
    
    path('', ImovelListView.as_view(), name='lista_imoveis'),
    path('imovel/<int:pk>/', ImovelDetailView.as_view(), name='detalhe_imovel'),
    path('imovel/novo/', ImovelCreateView.as_view(), name='criar_imovel'),
    path('imovel/<int:pk>/editar/', ImovelUpdateView.as_view(), name='editar_imovel'),
    path('imovel/<int:pk>/deletar/', ImovelDeleteView.as_view(), name='deletar_imovel'),
    
    
    path('api/', include(router.urls)),
]
