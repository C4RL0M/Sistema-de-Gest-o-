# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:42:02 2020

@author: User
"""

geral = []
pessoa = {}
print("1-Cadastrar pessoa")
print("2-Lista Cadastros")
print("3-Procurar Pessoa Especifica")
print("4-Encerrar")
op = input("Digite a opção desejada: ")
while op !="4":
    if op == '1':     
        pessoa ['nome'] = input("informe o nome do cliente: ")
        pessoa ['idade'] = input("informe a idade do cliente: ")
        pessoa ['cep'] = input("informe o cep do cliente: ")
        perg = 's'
        perg = input("quer cadastrar outro? S/N  ")
        geral.append(pessoa.copy())
        if perg in 'sS':
            pessoa.clear()
            continue
        if perg in 'Nn':
            pessoa.clear()
            print("1-Cadastrar pessoa")
            print("2-Lista Cadastros")
            print("3-Procurar Pessoa Especifica")
            print("4-Encerrar")
            op = input("Digite a opção desejada: ")
    if op == '2':
        for pessoa in geral:
            print(pessoa)
        p = 's'
        p = input("quer escolher outra opção? S/N  ")
        if p in 'Ss':
            print("1-Cadastrar pessoa")
            print("2-Lista Cadastros")
            print("3-Procurar Pessoa Especifica")
            print("4-Encerrar")
            op = input("Digite a opção desejada: ")
        if p in 'nN':
            break                
    if op == '3':
        busca = input("Digite o nome do cliente que deseja buscar:  ")
        for pessoa in geral:
            if busca == pessoa ['nome']:
                for k,v in pessoa.items():
                    print (f"{v}")
        p = 's'
        p = input("quer escolher outra opção? S/N  ")
        if p in 'Ss':
            print("1-Cadastrar pessoa")
            print("2-Lista Cadastros")
            print("3-Procurar Pessoa Especifica")
            print("4-Encerrar")
            op = input("Digite a opção desejada: ")
        if p in 'nN':
            break
    if op not in '1234':
        print("digite apenas 1, 2, 3 ou 4")
        print("1-Cadastrar pessoa")
        print("2-Lista Cadastros")
        print("3-Procurar Pessoa Especifica")
        print("4-Encerrar")
        op = input("Digite a opção desejada: ") 
print("Obrigado!")