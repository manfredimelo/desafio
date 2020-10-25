from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from base.menu import get_list


@login_required(login_url='/')
def index(request):
    menu = get_list('Dashboard')

    return render(request, 'base/index.html', locals())
