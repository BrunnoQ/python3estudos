import time

def menu():
	flag_sistema = True
	
	while flag_sistema:
		menu = """Escolha uma opção:
		1] SOMAR
		2] SUBTRAIR
		3] MULTIPLICAR
		4] DIVIDIR
		0] SAIR
		Opção: """
	
		opcao = input(menu)
	
		if opcao == "1":
			print("SOMA selecionado")
			somar()

		elif opcao == "2":
			print("SUBTRAIR Selecionado")
			subtrair()
	
		elif opcao == "3":
			print("MULTIPLICAR Selecionado")
			multiplicar()	
	
		elif opcao == "4":
			print("DIVIDIR Selecionado")
			dividir()
	
		elif opcao == "0":
			print("SAIR Selecionado...")
			time.sleep(3)
			exit()
		else:
			print("opção invalida!")
			time.sleep(3)

def somar():
	numero1 = float(input("Informe o primeiro numero:"))
	numero2 = float(input("Informe o segundo numero:"))
	resultado = numero1 + numero2
	print("Resultado da SOMA {0}".format(resultado))
	
def subtrair():
	numero1 = float(input("Informe o primeiro numero:"))
	numero2 = float(input("Informe o segundo numero:"))
	resultado = numero1 - numero2
	print("Resultado da SUBTRAÇÃO {0}".format(resultado))
	
def multiplicar():
	numero1 = float(input("Informe o primeiro numero:"))
	numero2 = float(input("Informe o segundo numero:"))
	resultado = numero1 * numero2
	print("Resultado da MULTIPLICAÇÃO {0}".format(resultado))
	
def dividir():
	numero1 = float(input("Informe o primeiro numero:"))
	numero2 = float(input("Informe o segundo numero:"))
	resultado = numero1 / numero2
	print("Resultado da DIVISÃO {0}".format(resultado))

	
#if opcao_menu not in '1234'
#exit()

menu()


