from django.shortcuts import render, redirect
from .models import Pessoa, Endereco
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
    pessoas = Pessoa.objects.all()
    endereco = Endereco.objects.get(pessoa=id)
    pessoa.data_nascimento = dt.datetime.strftime(pessoa.data_nascimento, "%Y-%m-%d")
    return render(request, 'update.html', {'pessoa': pessoa, 'pessoas':pessoas, 'endereco':endereco})


def update(request, id):         
    nome = request.POST.get('nome')
    data_nascimento = request.POST.get('data_nascimento')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    
    logradouro = request.POST.get('logradouro')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    pessoa_id = request.POST.get('pessoa_id')
    
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.cpf = cpf
    pessoa.rg = rg
    pessoa.data_nascimento = data_nascimento
    pessoa.save()
    
    endereco = Endereco.objects.get(pessoa=id)
    endereco.logradouro = logradouro
    endereco.numero = numero
    endereco.bairro = bairro
    endereco.pessoa = pessoa
    endereco.save()
    
    return redirect(home)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)


def salvar_endereco(request):
    logradouro = request.POST.get('logradouro')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    pessoa_id = int(request.POST.get('pessoa_id'))
    pessoa = Pessoa.objects.get(id=pessoa_id)
    
    Endereco.objects.create(logradouro=logradouro, numero=numero, bairro=bairro, pessoa=pessoa)
    
    return redirect(home)
