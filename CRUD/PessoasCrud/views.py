from django.shortcuts import render, redirect
from .models import Pessoa
import datetime as dt


# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})


def salvar(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    data_nascimento = request.POST.get('data_nascimento')

    Pessoa.objects.create(nome=nome, cpf=cpf, rg=rg, data_nascimento=data_nascimento)

    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})


def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa': pessoa})


def update(request, id):
    nome = request.POST.get('nome')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.save()
    return redirect(home)


def deletar(request, id):
    pessoa = Pessoa.objects.get(id)
    pessoa.delete()
    return redirect(home)
