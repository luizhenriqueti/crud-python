from django.db import models


class Pessoa(models.Model):
    #id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    nome = models.CharField(max_length=150)
    numero = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome