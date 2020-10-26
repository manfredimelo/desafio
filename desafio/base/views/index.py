from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from base.menu import get_list
from base.observer import analise_classificao


@login_required(login_url='/')
def index(request):
    menu = get_list('Dashboard')
    analise_classificao()
    return render(request, 'base/index.html', locals())
