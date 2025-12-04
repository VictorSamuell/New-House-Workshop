"""
Script para popular a base de dados da CasaNova com dados de teste.
Execute com: python populate_db.py
"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CasaNova'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CasaNova.settings')
django.setup()

from imoveis.models import Corretor, Imovel
from django.contrib.auth.models import User

def populate_database():
    print("🏗️  Iniciando população da base de dados...")
    
    # Obter usuário admin
    user = User.objects.get_or_create(username='admin')[0]
    
    # Criar corretores
    corretores_data = [
        {
            'nome': 'João Silva',
            'creci': '123456789',
            'telefone': '+351 91 234 5678'
        },
        {
            'nome': 'Maria Santos',
            'creci': '987654321',
            'telefone': '+351 91 987 6543'
        },
        {
            'nome': 'Pedro Oliveira',
            'creci': '555666777',
            'telefone': '+351 91 555 4433'
        },
    ]
    
    corretores = []
    for data in corretores_data:
        corretor, created = Corretor.objects.get_or_create(
            creci=data['creci'],
            defaults={'nome': data['nome'], 'telefone': data['telefone']}
        )
        if created:
            print(f"✓ Corretor criado: {corretor.nome}")
        else:
            print(f"- Corretor já existe: {corretor.nome}")
        corretores.append(corretor)
    
    # Criar imóveis
    imoveis_data = [
        {
            'titulo': 'Apartamento Moderno no Centro',
            'descricao': 'Apartamento com 3 quartos, cozinha equipada e varanda com vista.',
            'preco': 350000.00,
            'disponivel': True,
            'corretor': corretores[0]
        },
        {
            'titulo': 'Moradia Espaçosa em Zona Residencial',
            'descricao': 'Moradia com 4 quartos, piscina e garagem para 2 carros.',
            'preco': 550000.00,
            'disponivel': True,
            'corretor': corretores[1]
        },
        {
            'titulo': 'Estúdio em Zona Comercial',
            'descricao': 'Estúdio compacto ideal para investimento.',
            'preco': 150000.00,
            'disponivel': False,
            'corretor': corretores[2]
        },
        {
            'titulo': 'Penthouse Luxuoso com Vista para o Rio',
            'descricao': 'Penthouse de luxo com acabamentos premium.',
            'preco': 950000.00,
            'disponivel': True,
            'corretor': corretores[0]
        },
        {
            'titulo': 'Apartamento T2 Confortável',
            'descricao': 'Apartamento aconchegante com 2 quartos e terraço.',
            'preco': 250000.00,
            'disponivel': True,
            'corretor': corretores[1]
        },
    ]
    
    for data in imoveis_data:
        imovel, created = Imovel.objects.get_or_create(
            titulo=data['titulo'],
            defaults={
                'descricao': data['descricao'],
                'preco': data['preco'],
                'disponivel': data['disponivel'],
                'corretor': data['corretor'],
                'criado_por': user
            }
        )
        if created:
            comissao = imovel.calcular_comissao()
            print(f"✓ Imóvel criado: {imovel.titulo} - €{imovel.preco} (Comissão: €{comissao:.2f})")
        else:
            print(f"- Imóvel já existe: {imovel.titulo}")
    
    # Resumo
    print("\n" + "="*60)
    print("✅ Resumo da População:")
    print(f"  • Corretores: {Corretor.objects.count()}")
    print(f"  • Imóveis: {Imovel.objects.count()}")
    print(f"  • Imóveis Disponíveis: {Imovel.objects.filter(disponivel=True).count()}")
    print(f"  • Valor Total em Imóveis: €{sum(i.preco for i in Imovel.objects.all()):.2f}")
    print(f"  • Comissões Totais (5%): €{sum(i.calcular_comissao() for i in Imovel.objects.all()):.2f}")
    print("="*60)

if __name__ == '__main__':
    populate_database()
