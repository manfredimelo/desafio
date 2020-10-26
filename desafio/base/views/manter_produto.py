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
            nome = request.get('nome')
            cor = request.get('cor')
            tipo = request.get('tipo')
            processado = request.get('processado')

            if nome:
                produtos = produtos.filter(nome__icontains=nome)
            if cor:
                produtos = produtos.filter(nome__icontains=cor)
            if tipo:
                produtos = produtos.filter(tipo__icontains=tipo)

            if processado and processado == "SIM":
                produtos = produtos.filter(processado=True)
            elif processado and processado == "NAO":
                produtos = produtos.filter(processado=False)

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


def classificacao_produto(request, id_produto):
    menu = get_list('Produtos')
    produto = Produto.objects.get(pk=id_produto)

    return render(request, 'produto/classificacao_produto.html', locals())