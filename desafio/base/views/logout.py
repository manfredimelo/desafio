# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib import auth as django_auth
from django.shortcuts import redirect


# @login_required
def logout(request, ):
    django_auth.logout(request)
    return redirect('/')