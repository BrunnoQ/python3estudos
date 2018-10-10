#! /usr/bin/python

numero = int(input("Digite um numero: "))
if numero > 5:
	print("Numero maior que cinco!")
elif numero == 5:
	print("Numero igual a cinco!")
else:
	print("Numero menor que cinco!")
	
#Criar tupla Imutavel
tupla = (1,2,'Porto',3.4)
print(tupla[3])
print("Tamanho da Tupla: ",len(tupla))

# Percorrer Tupla
tupla = (0,1,2,3,4,5,6,7,8,9)

for n in tupla:
	if n % 2 == 0:
		print("{} é um número par" .format(n))
	else:
		print("{} é um número impar" .format(n))

#Slice
print(tupla[:])#varre toda a lista
print(tupla[0:6])#exibe do 0 ao 5
print(tupla[0:10:2])#exibe do 0 ao 5 pulando de 2 em 2

#Nao ler o \n em strings
nome = 'Porto 4Lixu Seguro\n'
print(nome[:-1])

#Strip
nome = '00000000000000Porto 4Lixu Seguro'
print(nome.strip("0"))

#Técnica chamada de descompressão
versao, path, build = 3.2, '/tmp', 'v1'
# Exercicio de cadastro de nomes
nomes = []
for i in range(4):
	nome = input("Informe o nome: ")
	nomes.append(nome)
	
print("Nomes adicionados",nomes)

#Mostrar nomes percorrendo lista
for n in nomes:
	print(n)
	
print("\n".join(nomes))

#Exibir a ordem da lista do peao
for n in nomes:
	print(nomes.index(n),n)
	
for i in range(len(nomes)):
	print(i,nomes[i])
	
for i in enumerate(nomes):
	print(i)
	
for key, value in enumerate(nomes):
	print(key, value)

for key, value in enumerate(nomes):
	print("ID: {0} Nome: {1}".format(key, value))

for t in enumerate(nomes):
	print("ID: {0[0]} Nome: {0[1]}".format(t))

#Tabular com format
for t in enumerate(nomes):
	print("ID: {0[0]:.>10} Nome: {0[1]:.>10}".format(t))

#Dicionario chave => valor, chave ->valor
dicionario = {"nome" : "Hector","Idade" : 27}
print(dicionario['nome'])

estranho = ({'id' : 1, 'nome' : 'Hector'},{'id' : 2, 'nome' : 'Paula'},{'id' : 3, 'nome' : 'Joana'})
print(estranho[2]['nome'])