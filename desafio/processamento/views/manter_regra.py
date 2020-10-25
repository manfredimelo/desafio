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

from base.menu import get_list
from processamento.forms.regra_buscar_form import RegraBuscarForm
from processamento.forms.regra_form import RegraForm
from processamento.models import Regra


class RegraListView(PermissionRequiredMixin, ListView):

    model = Regra
    form_class = RegraBuscarForm
    template_name = "regra/listagem.html"
    permission_required = 'processamento.add_regra'
    permission_denied_message = 'Você não tem permissão para acessar essa pagina.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        regras = self.get_queryset().distinct()
        context['buscar_form'] = self.form_class(self.request.GET)
        context['regras'] = regras
        context['total_regras'] = regras.count()
        page = int(self.request.GET.get('regras_page', 1))
        context['regras_paginator'] = Paginator(regras, 25).page(page)
        context['menu'] = get_list('Regras', self.request.user)
        return context

    def get_queryset(self):
        request = self.request.GET
        regras = super(RegraListView, self).get_queryset().all().order_by('id')
        buscar_form = self.form_class(self.request.GET)
        if buscar_form.is_valid():
            campo = request.get('campo')
            valor = request.get('valor')

            if campo:
                regras = regras.filter(campo__icontains=campo)
            if valor:
                regras = regras.filter(valor__icontains=valor)

        return regras


class RegraCreateView(CreateView):
    model = Regra
    form_class = RegraForm
    template_name = "regra/formulario.html"
    permission_required = 'processamento.add_regra'

    @method_decorator(login_required)
    def get(self, request):
        regra_form = self.form_class(use_required_attribute=False)
        menu = get_list('Regras', self.request.user)

        return render(request, self.template_name, context=locals())

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        regra_form = self.form_class(request.POST, use_required_attribute=False)
        menu = get_list('Regras', self.request.user)

        if regra_form.is_valid():
            regra = regra_form.save()
            messages.success(request,
                             '<strong> Regra </strong> foi salva com sucesso. ')
            return redirect(reverse('listar_regras'))

        return render(request, self.template_name, context=locals())




class RegraUpdateView(UpdateView):
    model = Regra
    form_class = RegraForm
    template_name = "regra/formulario.html"
    permission_required = 'processamento.edit_regra'

    # group_required = []

    @method_decorator(login_required)
    def get(self, request, id_regra):
        regra = Regra.objects.get(pk=id_regra)
        usuario_logado = self.request.user
        menu = get_list('Regras', self.request.user)

        regra_form = self.form_class(instance=regra)

        return render(request, self.template_name, context=locals())

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        id_regra = kwargs['id_regra']
        regra = get_object_or_404(Regra, pk=id_regra)
        regra_form = self.form_class(request.POST, instance=regra)

        usuario_logado = self.request.user

        if regra_form.is_valid():
            regra = regra_form.save(commit=False)
            regra.save()

            messages.success(request, '<strong> Regra</strong> foi atualizadacom sucesso. ')
            return redirect(reverse('listar_regras'))

        return render(request, self.template_name, context=locals())
