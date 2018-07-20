import cadfunc
import time

def menu_in():	
	while True:
		print ("#################################")
		print ("#### Pilot Jarvis Paraguaio  ####")
		print ("####           Menu          ####")
		print ("#Selecione uma das opções abaixo#")
		print ("# 1- Cadastrar                  #")
		print ("# 2- Procurar                   #")
		print ("# 3- Listar                     #")
		print ("# 4- Alterar                    #")
		print ("# 5- Ordernar                   #")
		print ("# 6- Remover                    #")
		print ("# CTRL+C - SAIR                 #")
		print ("#################################")
		
		try:
			opcao = input("Opção: ")
			if opcao == "1":
				print("# CADASTRAMENTO SELECIONADO #")
				nome_usuario = str.upper(input("Informe o nome do usuário: "))
				cadfunc.inserir_usuario(nome_usuario)
			
			elif opcao == "2":
				print("# PROCURAR SELECIONADO #")
				nome_pesquisar = str.upper(input("Informe o nome do usuário a ser pesquisado: "))
				cadfunc.pesquisar_usuario(nome_pesquisar)
			
			elif opcao == "3":
				print("# LISTAR SELECIONADO #")
				cadfunc.listar_usuarios()
			
			elif opcao == "4":
				print("# ALTERAR SELECIONADO #")
				id_usuario = str.upper("{0:0>4}".format(input("Informe o ID do usuário: ")))
				cadfunc.atualizar_usuario(id_usuario)
				
			elif opcao == "5":
				print("# ORDENAR SELECIONADO #")
				cadfunc.ordernar_cadastro_por_id()
				
			elif opcao == "6":
				print ("# ORDERNAR ALFA SELECIONADO")
			
			time.sleep(2)#Para não estourar a memória
		
		except KeyboardInterrupt as e:
			print("Fechando Conexões.....",e)
			exit()

menu_in()
		