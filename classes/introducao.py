class Humano():
	
	#Método construtor CALL ARGS
	#def __init__(self,**param):
	#	self.peso = param["peso"]
	#	self.cor = param["cor"]
	#	self.altura = param["altura"]
	#	self.forca = param["forca"]
	#	self.nome = param["nome"]
	#	self.sexo = param["sexo"]
	
	
	#Método construtor
	def __init__(self, peso=0, cor="Cinza", altura=0, forca=0, nome=" ", sexo="F"):
		self.peso = peso
		self.cor = cor
		self.altura = altura
		self.forca = forca
		self.nome = nome
		self.sexo = sexo
	
	def __str__(self):
		return "{0} -> Peso: {1} e Altura {2} do sexo {3}".format(self.nome,self.peso,self.altura,self.sexo)
	
	def comer(self, comida):
		self.peso += 1.50
		print("{0} esta comendo {1}".format(self.nome, comida))

class Homem(Humano):
	#Sobrecarga do método construtor
	def __init__(self, **kwargs):
		self.sexo = "Masculino"
		super(Homem, self).__init__(**kwargs)#supressao dos parametros a serem passados

humano = Humano()
print(type(humano))

homem = Humano(peso=82, altura=1.80,nome="Brunno",sexo="Masculino")
brunno = Homem(peso=86, altura=1.80,nome="Brunno",sexo="Masculino")
homem.comer("Miojo")
brunno.comer("Carne")
print(homem)
print(brunno)