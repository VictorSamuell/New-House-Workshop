from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Imovel, Corretor
from .forms import ImovelForm
from .serializers import ImovelSerializer
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CorretorListView(ListView):
    model = Corretor
    template_name = 'corretor_list.html'
    context_object_name = 'corretores'
    paginate_by = 10


class CorretorDetailView(LoginRequiredMixin ,DetailView):
    model = Corretor
    template_name = 'corretor_detail.html'
    context_object_name = 'corretor'


class CorretorCreateView(LoginRequiredMixin, CreateView):
    model = Corretor
    fields = ['nome', 'creci', 'telefone']
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('lista_corretores')


class CorretorUpdateView(LoginRequiredMixin ,UpdateView):
    model = Corretor
    fields = ['nome', 'creci', 'telefone']
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('lista_corretores')


class CorretorDeleteView(LoginRequiredMixin ,DeleteView):
    model = Corretor
    template_name = 'corretor_confirm_delete.html'
    success_url = reverse_lazy('lista_corretores')



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


class ImovelCreateView(LoginRequiredMixin, CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('lista_imoveis')


class ImovelUpdateView(LoginRequiredMixin ,UpdateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('lista_imoveis')


class ImovelDeleteView(LoginRequiredMixin, DeleteView):
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


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')