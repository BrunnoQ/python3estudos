
class CSV():
	#Construtor
	def __init__(self, path, arquivo):
		self.path = path
		self.arquivo = arquivo
		
	def exibir(self):
		registro_imprimir=[]
		with open(self.path+self.arquivo,"r") as arquivo:
			for linha in arquivo:
				id_usuario, nome_usuario = linha.split(";")
				registro_imprimir.append("{0:0>4};{1}".format(id_usuario, nome_usuario))	
		
		print("#################################")
		print("##### Usuárias Cadastradas ######")
		print("\n".join(registro_imprimir)+"\n")
		print("Total Usuárias Cadastradas: ",len(registro_imprimir))
		print("#################################")

csv = CSV("D:\\sinais\\","usuarios.csv")
csv.exibir()