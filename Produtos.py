# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:36:08 2020

@author: User
"""

pesquisa = []
produtos = []

nome= input("digite o nome do produto: ")
while nome !="":
    loja = input("digite o nome da loja: ")
    preço = input("digite o preço do produto: R$  ")
    perg = 's'
    perg = input("quer buscar esse produto em outra loja? S/N   ")
    produtos.append(nome)
    produtos.append(loja)
    produtos.append(preço)
    while perg not in 'nN':
        loja2 = input("digite a outra loja: ")
        produtos.append(loja2)
        preço2 = input("digite o outro preço: R$  ")
        produtos.append(preço2) 
        pesquisa.append(produtos.copy())
        produtos.clear()
        perg = input("quer buscar esse produto em outra loja? S/N   ")
    nome= input("digite o nome de outro produto: ")
resp = 's'
while resp not in 'nN':
    busca = input("digite o nome do produto que deseja buscar: ")
    print(pesquisa)       
    resp = input("quer consultar outro S/N:  ")
    if resp in "Ss":
        continue
    elif resp not in "SsNn":
        print("digite apenas S ou N")
        resp = input("quer consultar outro S/N:  ")
    elif resp in "Nn":
        break
print(" <<< ENCERRADO >>> ")