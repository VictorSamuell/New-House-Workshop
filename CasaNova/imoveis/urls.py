from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ImovelListView, ImovelDetailView, ImovelCreateView,
    ImovelUpdateView, ImovelDeleteView, ImovelViewSet,
    CorretorListView, CorretorDetailView, CorretorCreateView,
    CorretorUpdateView, CorretorDeleteView , RegisterView
)

router = DefaultRouter()
# imovel viewset para a API do serializer
router.register(r'imoveis', ImovelViewSet, basename='imovel')

urlpatterns = [
# rotas do corretor
    path('corretores/', CorretorListView.as_view(), name='lista_corretores'),
    path('corretor/<int:pk>/', CorretorDetailView.as_view(), name='detalhe_corretor'),
    path('corretor/novo/', CorretorCreateView.as_view(), name='criar_corretor'),
    path('corretor/<int:pk>/editar/', CorretorUpdateView.as_view(), name='editar_corretor'),
    path('corretor/<int:pk>/deletar/', CorretorDeleteView.as_view(), name='deletar_corretor'),
    
# rotas do imovel
    path('', ImovelListView.as_view(), name='lista_imoveis'),
    path('imovel/<int:pk>/', ImovelDetailView.as_view(), name='detalhe_imovel'),
    path('imovel/novo/', ImovelCreateView.as_view(), name='criar_imovel'),
    path('imovel/<int:pk>/editar/', ImovelUpdateView.as_view(), name='editar_imovel'),
    path('imovel/<int:pk>/deletar/', ImovelDeleteView.as_view(), name='deletar_imovel'),
    
# preparando para a rota da API
    path('api/', include(router.urls)),
    
# rota register
    path('register/', RegisterView.as_view(), name='register'),
    
]
