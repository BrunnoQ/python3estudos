import time
import random
import os
import winsound

def inserir_usuario(nome_usuario):
	"""Insere um usuario num arquivo csv.
	   Bipa um som e lista os usuarios cadastrados
	   no arquivo."""
	id_usuario = 0
	if nome_usuario != "":
		id_usuario = random.randrange(1000)
		with open("D:\\sinais\\usuarios.csv","a") as file:
			file.write("{0:0>4} - {1}\n".format(id_usuario,nome_usuario+";"))
			
	else:
		print("Informe o nome do usuário animal!")
	
	print("Usuária Cadastrada!")
	#winsound.Beep(1000,2000)
	os.system("cls")
	listar_usuarios()
		
def pesquisar_usuario(nome_pesquisar):
	"""Recebe o nome a ser pesquisado e printa na tela.
	   Bipa um som."""
	nao_encontrou_flag = True
	with open("D:\\sinais\\usuarios.csv","r") as arquivo:
		for linha in arquivo:
			if nome_pesquisar in linha:
				print("Usuária cadastrada: ",linha)
				nao_encontrou_flag = False
	
	if(nao_encontrou_flag):
		print(nome_pesquisar+" não está cadastrado.")

	#winsound.Beep(1500,2000)

def listar_usuarios():
	"""Lista os usuarios cadastrados no arquivo csv.
	   Bipa um som."""
	registro_imprimir = []
	with open("D:\\sinais\\usuarios.csv","r") as arquivo:
		for linha in arquivo:
			id_usuario, nome_usuario = linha.split(";")
			registro_imprimir.append("{0:0>4};{1}".format(id_usuario, nome_usuario))
			
	os.system("cls")
	print("#################################")
	print("##### Usuárias Cadastradas ######")
	print("\n".join(registro_imprimir)+"\n")
	print("Total Usuárias Cadastradas: ",len(registro_imprimir))
	print("#################################")
	#winsound.Beep(2000,2000)
	
def atualizar_usuario(id_usuario):
	"""Recebe o ID da Usuária e atualiza o nome da mesma conforme o informado
	   pelo usuário.
	   Bipa um som."""
	print("Pesquisando usuários....")
	linhas = []
	with open("D:\\sinais\\usuarios.csv","r+") as arquivo:
		linhas = arquivo.readlines()
		nao_achou_flag = True
		#BUSCA LINEAR PORCA!
		for contador , valor in enumerate(linhas):
			if id_usuario in str(valor):
				os.system("cls")
				print("Usuária Encontrada! ",valor)
				nome_atualizado = str.upper(input("Informe o novo nome da usuaria: "))
				linhas[contador] = "{0:0>4} - {1}\n".format(id_usuario,nome_atualizado+";")
				arquivo.writelines(linhas)
				nao_achou_flag = False
				
	if(nao_achou_flag):
		print("Usuária Não Encontrada!")

def ordernar_cadastro_por_id():
	"""Ordenar de forma Crescente / Decrescente o cadastro das usuárias.
	   Bipa um som."""
	lista_ordenada = []
	with open("D:\\sinais\\usuarios.csv","r") as arquivo:
		linhas = arquivo.readlines()
		opcao_ordenacao = str(input("Ordenar / Crescente ou Decrescente? ")).upper()
		
		if opcao_ordenacao == "C":
			lista_ordenada = sorted(linhas)
			print("##### Usuárias ordenadas de forma CRESCENTE ######")
			print("\n".join(lista_ordenada)+"\n")
			with open("D:\\sinais\\usuarios.csv","w") as arquivo:
				arquivo.writelines(lista_ordenada)
			
		elif opcao_ordenacao == "D":
			lista_ordenada = sorted(linhas, reverse=True)
			print("##### Usuárias ordenadas de forma DECRESCENTE ######")
			print("\n".join(lista_ordenada)+"\n")
			with open("D:\\sinais\\usuarios.csv","w") as arquivo:
				arquivo.writelines(lista_ordenada)
				

				
			
				
			
	