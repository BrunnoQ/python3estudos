# -*- coding: UTF-8 -*-
#! /usr/bin/python
#Ler arquivo
#Com o with o arquivo fecha automaticamente
with open("D:\\sinais\\python.txt","a") as arquivo:
	for i in range(1):
		arquivo.write("{0} - {1}\n".format(i,"Item"))
print("Fim arquivo")
linhas = []

with open("D:\\sinais\\usuarios.csv","r") as f:
	for linha in f:
		id, nome = linha.split(";")
		print(nome)
		nome = linha.strip().title()
		linhas.append("{0:0>2};{1}".format(id, nome))
	
print("\n".join(linhas)+"\n")
	
with open("D:\\sinais\\usuarios.csv","w") as file:
	file.write("\n".join(linhas)+"\n")
		