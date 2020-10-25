from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from base.forms.produto_buscar_form import ProdutoBuscarForm
from base.forms.produto_form import ProdutoForm
from base.menu import get_list
from base.models import Produto


class ProdutoListView(PermissionRequiredMixin, ListView):

    model = Produto
    form_class = ProdutoBuscarForm
    template_name = "produto/listagem.html"
    permission_required = 'base.add_produto'
    permission_denied_message = 'Você não tem permissão para acessar essa pagina.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = self.get_queryset().distinct()
        context['buscar_form'] = self.form_class(self.request.GET)
        context['produtos'] = produtos
        context['total_produtos'] = produtos.count()
        page = int(self.request.GET.get('produtos_page', 1))
        context['produtos_paginator'] = Paginator(produtos, 25).page(page)
        context['menu'] = get_list('Produtos', self.request.user)
        return context

    def get_queryset(self):
        request = self.request.GET
        produtos = super(ProdutoListView, self).get_queryset().all().order_by('id')
        buscar_form = self.form_class(self.request.GET)
        if buscar_form.is_valid():
            id = request.get('id')
            # nome_fantasia = request.get('nome_fantasia')
            # id_regiao = request.get('regiao')
            # # status = request.get('status')
            # cnpj = request.get('cnpj')
            #
            # if cnpj:
            #     hoteis = hoteis.filter(Q(cnpj__icontains=cnpj))
            # if nome_fantasia:
            #     hoteis = hoteis.filter(Q(nome_fantasia__icontains=nome_fantasia))
            # if id_regiao:
            #     hoteis = hoteis.filter(regiao=id_regiao)

        return produtos


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto/formulario.html"
    permission_required = 'base.add_produto'

    @method_decorator(login_required)
    def get(self, request):
        produto_form = self.form_class(use_required_attribute=False)
        menu = get_list('Produtos', self.request.user)

        return render(request, self.template_name, context=locals())

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        produto_form = self.form_class(request.POST, use_required_attribute=False)
        menu = get_list('Produtos', self.request.user)

        if produto_form.is_valid():
            produto = produto_form.save()
            messages.success(request,
                             '<strong>' + produto.nome + '</strong> foi salvo com sucesso. ')
            return redirect(reverse('listar_produtos'))

        return render(request, self.template_name, context=locals())




class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto/formulario.html"
    permission_required = 'base.edit_produto'

    # group_required = []

    @method_decorator(login_required)
    def get(self, request, id_produto):
        produto = Produto.objects.get(pk=id_produto)
        usuario_logado = self.request.user
        menu = get_list('Produtos', self.request.user)

        produto_form = self.form_class(instance=produto)

        return render(request, self.template_name, context=locals())

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        id_produto = kwargs['id_produto']
        produto = get_object_or_404(Produto, pk=id_produto)
        produto_form = self.form_class(request.POST, instance=produto)

        usuario_logado = self.request.user

        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.save()

            messages.success(request, '<strong> {} </strong> foi atualizado com sucesso. '.format(produto.nome))
            return redirect(reverse('listar_produtos'))

        return render(request, self.template_name, context=locals())
#
#
# # @permission_required('painel.add_hotel')
# class HotelDeleteView(DeleteView):
#     permission_required = 'painel.add_hotel'
#
#     @method_decorator(login_required)
#     def get(self, request, id_hotel):
#         usuario_logado = self.request.user
#         hotel = get_object_or_404(Hotel, pk=id_hotel)
#
#         if hotel:
#             hotel.is_active = False
#             hotel.save()
#             messages.success(request, '<strong>' + hotel.nome + '</strong> foi desativado com sucesso. ')
#             return redirect(reverse('listar_hoteis'))
#
#         return render(request, self.template_name, context=locals())
