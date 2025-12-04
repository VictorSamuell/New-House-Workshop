from rest_framework import serializers
from .models import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    # Campo para leitura (nome do corretor)
    corretor_nome = serializers.StringRelatedField(source='corretor', read_only=True)
    
    class Meta:
        model = Imovel
        fields = [
            'id', 'titulo', 'descricao', 'preco', 'foto_principal', 'disponivel',
            'corretor',      # ID para escrita (POST)
            'corretor_nome', # Nome para leitura (GET)
            'criado_por'
        ]
