from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Imovel
from .forms import ImovelForm
from .serializers import ImovelSerializer

class ImovelListView(ListView):
    model = Imovel
    template_name = 'imovel_list.html'
    context_object_name = 'imoveis'
    paginate_by = 10

    def get_queryset(self):
        return Imovel.objects.filter(disponivel=True)

class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'imovel_detail.html'
    context_object_name = 'imovel'


class ImovelCreateView(CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('lista_imoveis')


class ImovelUpdateView(UpdateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('lista_imoveis')


class ImovelDeleteView(DeleteView):
    model = Imovel
    template_name = 'imovel_confirm_delete.html'
    success_url = reverse_lazy('lista_imoveis')


class ImovelViewSet(viewsets.ModelViewSet):
    serializer_class = ImovelSerializer

    def get_queryset(self):
        queryset = Imovel.objects.all()
    
        disponivel = self.request.query_params.get('disponivel')
        preco_max = self.request.query_params.get('preco_max')
        
        if disponivel and disponivel.lower() == 'true':
            queryset = queryset.filter(disponivel=True)
            
       
        if preco_max:
            queryset = queryset.filter(preco__lte=preco_max)
            
        return queryset
