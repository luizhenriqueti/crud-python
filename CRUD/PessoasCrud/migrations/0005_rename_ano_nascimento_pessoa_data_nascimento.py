# Generated by Django 4.1 on 2022-08-29 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PessoasCrud', '0004_rename_idade_pessoa_ano_nascimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='ano_nascimento',
            new_name='data_nascimento',
        ),
    ]
