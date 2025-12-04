# Projeto Django "CasaNova" - Prova Prática

## ✅ Status: COMPLETO

---

## 📋 Questões Implementadas

### **Questão 1: Template Base** ✓
**Arquivo:** `templates/base.html`
- Carrega estáticos com `{% load static %}`
- Link para `css/style.css`
- Cabeçalho com título "CasaNova Imóveis"
- Bloco `{% block conteudo %}`

### **Questão 2: Formulário de Imóvel** ✓
**Arquivo:** `templates/imovel_form.html`
- Estende `base.html`
- Formulário multipart para upload de imagens: `enctype="multipart/form-data"`
- CSRF token incluído
- Botão "Salvar Imóvel"

### **Questão 3: View de Criação** ✓
**Arquivo:** `views.py` - `ImovelCreateView`
- Implementa `LoginRequiredMixin` - apenas utilizadores autenticados
- Sobrescreve `form_valid()` para associar `criado_por = self.request.user`
- Redireciona para 'lista_imoveis' após sucesso
- **Acesso:** `http://127.0.0.1:8000/imovel/novo/`

### **Questão 4: Serializer DRF** ✓
**Arquivo:** `serializers.py` - `ImovelSerializer`
- Inclui todos os campos do modelo
- Campo `corretor_nome` com `StringRelatedField` para mostrar nome do corretor
- Campos de entrada (ID do corretor) e leitura (nome do corretor)
- Suporta GET (leitura com nome) e POST (escrita com ID)

### **Questão 5: ViewSet com Filtros** ✓
**Arquivo:** `views.py` - `ImovelViewSet`
- Implementa `ModelViewSet` para CRUD completo
- Filtro 1: `?disponivel=true` - retorna apenas imóveis disponíveis
- Filtro 2: `?preco_max=500000` - retorna imóveis até ao preço máximo
- Filtros podem ser combinados: `?disponivel=true&preco_max=500000`

### **Questão 6: Configuração da API** ✓
**Arquivo:** `urls.py`
- `DefaultRouter` registado com ViewSet de Imóveis
- Endpoints disponíveis em `/api/imoveis/`
- CRUD completo via REST

### **Questão 7: Método de Comissão** ✓
**Arquivo:** `models.py` - Método na classe `Imovel`
```python
def calcular_comissao(self):
    if self.preco:
        return float(self.preco) * 0.05
    return 0.00
```
- Calcula 5% do preço
- Usado nos templates (ex: `{{ imovel.calcular_comissao }}`)

---

## 📂 Estrutura do Projeto

```
CasaNova/
├── CasaNova/                    # Projeto Django
│   ├── settings.py              # Configurações (SQLite)
│   ├── urls.py                  # URLs principais
│   └── wsgi.py
├── imoveis/                     # App principal
│   ├── models.py               # ✓ Modelos Corretor, Imovel
│   ├── views.py                # ✓ Views (ListView, DetailView, CreateView, etc.)
│   ├── forms.py                # ✓ ImovelForm
│   ├── serializers.py          # ✓ ImovelSerializer
│   ├── urls.py                 # ✓ Rotas (Web + API)
│   ├── admin.py                # ✓ Admin registado
│   └── templates/
│       ├── base.html           # ✓ Template base
│       ├── imovel_list.html    # ✓ Listagem com paginação
│       ├── imovel_detail.html  # ✓ Detalhes do imóvel
│       ├── imovel_form.html    # ✓ Formulário
│       └── imovel_confirm_delete.html  # ✓ Confirmação delete
├── static/
│   └── css/
│       └── style.css           # ✓ Estilos CSS responsivos
├── db.sqlite3                  # Base de dados
├── manage.py
├── criar_dados_teste.py        # ✓ Script para criar dados
└── API_TESTS.md                # ✓ Documentação de testes
```

---

## 🎯 Modelos de Dados

### **Corretor**
- `nome`: CharField
- `creci`: CharField (único)
- `telefone`: CharField

### **Imovel**
- `titulo`: CharField
- `descricao`: TextField
- `preco`: DecimalField
- `foto_principal`: ImageField (upload_to='imoveis/')
- `disponivel`: BooleanField (default=True)
- `corretor`: ForeignKey → Corretor (CASCADE)
- `criado_por`: ForeignKey → User (SET_NULL, null=True)

---

## 🌐 Rotas Disponíveis

### Web Views
| URL | View | Nome |
|-----|------|------|
| `/` | ImovelListView | lista_imoveis |
| `/imovel/<id>/` | ImovelDetailView | detalhe_imovel |
| `/imovel/novo/` | ImovelCreateView | criar_imovel |
| `/imovel/<id>/editar/` | ImovelUpdateView | editar_imovel |
| `/imovel/<id>/deletar/` | ImovelDeleteView | deletar_imovel |

### API REST (DefaultRouter)
| Método | URL | Ação |
|--------|-----|------|
| GET | `/api/imoveis/` | Listar todos |
| GET | `/api/imoveis/?disponivel=true` | Filtrar disponíveis |
| GET | `/api/imoveis/?preco_max=500000` | Filtrar por preço |
| GET | `/api/imoveis/<id>/` | Detalhes |
| POST | `/api/imoveis/` | Criar |
| PUT | `/api/imoveis/<id>/` | Atualizar |
| DELETE | `/api/imoveis/<id>/` | Deletar |

### Administrativa
| URL |
|-----|
| `/admin/` |
| `/api/` |

---

## 🚀 Como Executar

### 1. Instalar dependências (se necessário)
```bash
pip install django djangorestframework pillow django-cleanup
```

### 2. Criar dados de teste
```bash
python criar_dados_teste.py
```

### 3. Iniciar servidor
```bash
python manage.py runserver
```

### 4. Aceder ao projeto
- **Home:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/ (user: admin)
- **API:** http://127.0.0.1:8000/api/

---

## 📊 Dados de Teste Criados

**Corretor:**
- Nome: João Silva
- CRECI: 123456789
- Telefone: +351 91 234 5678

**Imóvel:**
- Título: Apartamento Moderno no Centro
- Preço: €350,000.00
- Comissão (5%): €17,500.00
- Status: Disponível

---

## 🎨 Features Adicionais Implementadas

✅ **ListView com Paginação** - Lista imóveis disponíveis com paginação (10 por página)
✅ **DetailView** - Mostra informações completas do imóvel
✅ **UpdateView** - Permite editar imóveis
✅ **DeleteView** - Confirmação antes de deletar
✅ **CSS Responsivo** - Design adaptável a diferentes tamanhos
✅ **Admin Django** - Gerenciamento completo via admin
✅ **Segurança** - LoginRequiredMixin nas views que precisam
✅ **Filtros API** - Combinação de múltiplos filtros
✅ **Script de Teste** - Dados pré-carregados

---

## 📝 Notas Importantes

- A base de dados usa **SQLite** para simplificar (originalmente MySQL)
- Todos os **campos obrigatórios** estão implementados
- O método `calcular_comissao()` é acessível em templates: `{{ imovel.calcular_comissao }}`
- O campo `criado_por` é preenchido automaticamente ao criar imóvel
- As imagens são armazenadas em `media/imoveis/`
- CSRF protection ativada em todos os formulários

---

## ✨ Pronto para Usar!

O projeto está **100% funcional** e **pronto para produção local**. Todas as questões foram implementadas conforme especificado.
