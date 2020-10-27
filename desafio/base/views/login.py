from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def login_restrito(request):
    user = request.user
    redirect_to = request.GET.get('next', 'index')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)

            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')
        else:
            if not usuario:
                messages.error(request, 'Login e/ou senha incorretos.')
            else:
                messages.error(request, 'Usuário sem permissão de acesso')
            return render(request, 'base/login.html')
    else:

        if request.user.id:
            return redirect('index')
        form_login = AuthenticationForm()
    return render(request, 'base/login.html', {'form_login': form_login})
