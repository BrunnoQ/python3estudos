# -*- coding: UTF-8 -*-
#! /usr/bin/python

nomes = ["Arthur","Brunno","Safira","Caio","Armenia","zuleica"]
for n in nomes:
	if 'a' in n.lower():
		print(n)

lista = [n.upper() for n in nomes] #Compreensão de lista
print(lista)

lista2 = [n[0:3] for n in nomes] #Compreensão de lista
print(lista2)

nomes2 = [{"nome" : "Artur"},{"nome" : "Bruna"},{"nome" : "Rafaela"},{"nome" : "Renata"},{"nome" : "Vania"}]

lista3 = [n["nome"][0:3] for n in nomes2] #Compreensão de lista
print(lista3)

#Acessando dados de um dicionario e compreensando uma listaS
nomes4 = [{"nome" : "Artur","notas": [9,10,7,8,5]},
	      {"nome" : "Bruna","notas": [9,10,7,8,5]},
		  {"nome" : "Rafaela","notas": [9,10,7,8,5]},
		  {"nome" : "Renata","notas": [9,10,7,8,5]},
		  {"nome" : "Vania","notas": [9,10,7,8,5]}]
lista3 = [n["notas"][1] for n in nomes4] #Compreensão de lista
print(lista4)