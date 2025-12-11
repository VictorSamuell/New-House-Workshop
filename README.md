# Projeto Django "CasaNova" - New House Workshop
---
---

## 📂 Estrutura do Projeto

```
CasaNova/
├── CasaNova/                    # Projeto Django
│   ├── settings.py              # Configurações 
│   ├── urls.py                  # URLs principais
│   └── wsgi.py
├── imoveis/                     # App principal
│   ├── models.py               #  Modelos Corretor, Imovel
│   ├── views.py                #  Views (ListView, DetailView, CreateView, etc.)
│   ├── forms.py                #  ImovelForm
│   ├── serializers.py          #  ImovelSerializer
│   ├── urls.py                 #  Rotas (Web + API)
│   ├── admin.py                #  Admin registado
│   └── templates/
│       ├── base.html           #  Template base
│       ├── imovel_list.html    #  Listagem com paginação
│       ├── imovel_detail.html  #  Detalhes do imóvel
│       ├── imovel_form.html    #  Formulário
│       └── imovel_confirm_delete.html  #  Confirmação delete
├── static/
│   └── css/
│       └── style.css           # Estilos CSS responsivos
├── db.sqlite3                  # Base de dados
├── manage.py
├── criar_dados_teste.py        # Script para criar dados
└── API_TESTS.md                # Documentação de testes
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
python manage.py makemigrations
python manage.py migrate

python populate_db.py
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

## 📊  Exemplos de Dados de Teste Criados

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


---

#

