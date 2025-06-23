from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class Login(View):
    def get(self, request):
        return render(request, 'autenticacao.html')

    def post(self, request):
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('criar-historias')  # ajuste conforme sua rota
        else:
            return render(request, 'autenticacao.html', {'erro': 'Usuário ou senha inválidos'})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
