def puts(*args):
	total = 0
	for i in args:
		total += i
	return total

#print(puts(1,2,3,4,5,6,7,8,0))

def eita(**kwargs):
	print("Nome: {}".format(kwargs["nome"]))
	print("Idade: {}".format(kwargs["idade"]))
	print("Peso: {}".format(kwargs["peso"]))
	
#eita("hector", 27, 60)

eita(idade=27, peso=60, nome="Brunno")