from rest_framework import serializers
from .models import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    
    corretor_nome = serializers.StringRelatedField(source='corretor', read_only=True)
    
    class Meta:
        model = Imovel
        fields = [
            'id', 
            'titulo', 
            'descricao', 
            'preco', 
            'foto_principal', 
            'disponivel',
            'corretor',      
            'corretor_nome', 
            'criado_por'
        ]
