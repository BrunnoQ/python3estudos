# -*- coding: utf-8 -*-
import time
import random
import os


def inserir_usuario(nome_usuario):
	"""Insere um usuario num arquivo csv.
	   Bipa um som e lista os usuarios cadastrados
	   no arquivo."""
	id_usuario = 0
	if nome_usuario != "":
		id_usuario = random.randrange(1000)
		with open("/home/brunno/Documentos/usuarios.csv","a") as file:
			file.write("{0:0>4} - {1}\n".format(id_usuario,nome_usuario+";"))
			
	else:
		print("Informe o nome do usuário animal!")
	
	print("Usuária Cadastrada!")
	
	os.system("cls")
	listar_usuarios()
		
def pesquisar_usuario(nome_pesquisar):
	"""Recebe o nome a ser pesquisado e printa na tela.
	   Bipa um som."""
	nao_encontrou_flag = True
	with open("/home/brunno/Documentos/usuarios.csv","r") as arquivo:
		for linha in arquivo:
			if nome_pesquisar in linha:
				print("Usuária cadastrada: ",linha)
				nao_encontrou_flag = False
	
	if(nao_encontrou_flag):
		print(nome_pesquisar+" não está cadastrado.")

def listar_usuarios():
	"""Lista os usuarios cadastrados no arquivo csv.
	   Bipa um som."""
	registro_imprimir = []
	with open("/home/brunno/Documentos/usuarios.csv","r") as arquivo:
		for linha in arquivo:
			id_usuario, nome_usuario = linha.split(";")
			registro_imprimir.append("{0:0>4};{1}".format(id_usuario, nome_usuario))
			
	os.system("cls")
	print("#################################")
	print("##### Usuárias Cadastradas ######")
	print("\n".join(registro_imprimir)+"\n")
	print("Total Usuárias Cadastradas: ",len(registro_imprimir))
	print("#################################")
	"""9000 vai no talo!"""
	
def atualizar_usuario(id_usuario):
	"""Recebe o ID da Usuária e atualiza o nome da mesma conforme o informado
	   pelo usuário.
	   Bipa um som."""
	print("Pesquisando usuários....")
	linhas = []
	with open("/home/brunno/Documentos/usuarios.csv","r") as arquivo:
		linhas = arquivo.readlines()
		nao_achou_flag = True
		#BUSCA LINEAR PORCA!
		for contador , valor in enumerate(linhas):
			if id_usuario in str(valor):
				os.system("cls")
				print("Usuária Encontrada! ",valor)
				nome_atualizado = str.upper(input("Informe o novo nome da usuaria: "))
				linhas[contador] = "{0:0>4} - {1}\n".format(id_usuario,nome_atualizado+";")

				with open("/home/brunno/Documentos/usuarios.csv","w") as arquivo2:
					arquivo2.writelines(linhas)
				
				nao_achou_flag = False
				
	if(nao_achou_flag):
		print("Usuária Não Encontrada!")

def remover_usuario(id_usuario):
	"""Recebe o ID da Usuária e renove a mesma da lista, conforme o informado
	   pelo usuário.
	   Bipa um som."""
	print("Pesquisando usuários....")
	linhas = []
	with open("/home/brunno/Documentos/usuarios.csv","r") as arquivo:
		linhas = arquivo.readlines()
		nao_achou_flag = True
		#BUSCA LINEAR PORCA!
		for contador , valor in enumerate(linhas):
			if id_usuario in str(valor):
				os.system("cls")
				linhas.pop(contador)
				with open("/home/brunno/Documentos/usuarios.csv","w") as arquivo2:
					arquivo2.writelines(linhas)							
				print("Usuária removida! ",valor)
				nao_achou_flag = False
				
	if(nao_achou_flag):
		print("Usuária Não Encontrada!")

def ordernar_cadastro_por_id():
	"""Ordenar de forma Crescente / Decrescente o cadastro das usuárias.
	   Bipa um som."""
	lista_ordenada = []
	with open("/home/brunno/Documentos/usuarios.csv","r") as arquivo:
		linhas = arquivo.readlines()
		opcao_ordenacao = str(input("Ordenar / Crescente ou Decrescente? ")).upper()
		
		if opcao_ordenacao == "C":
			lista_ordenada = sorted(linhas)
			print("##### Usuárias ordenadas de forma CRESCENTE ######")
			print("\n".join(lista_ordenada)+"\n")
			with open("/home/brunno/Documentos/usuarios.csv","w") as arquivo:
				arquivo.writelines(lista_ordenada)
			
		elif opcao_ordenacao == "D":
			lista_ordenada = sorted(linhas, reverse=True)
			print("##### Usuárias ordenadas de forma DECRESCENTE ######")
			print("\n".join(lista_ordenada)+"\n")
			with open("/home/brunno/Documentos/usuarios.csv","w") as arquivo:
				arquivo.writelines(lista_ordenada)
				

				
			
				
			
	