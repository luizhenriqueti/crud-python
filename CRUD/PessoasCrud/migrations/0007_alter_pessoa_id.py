# Generated by Django 4.1 on 2022-08-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PessoasCrud', '0006_alter_pessoa_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
