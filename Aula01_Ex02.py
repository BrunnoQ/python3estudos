# Receber o nome do Aluno
#Receber tres numeros do terminal, e exibir a media
# A média de Nome do Aluno é: VALOR
nome_aluno = input("Informe o nome do Aluno:")
notas = [0:3]
nota_count = 0
nota = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))
media = round((nota + nota2 + nota3) / 3,2)
print("A media do %s é: %s" %(nome_aluno,round(media,2)))
#Comentario
print("A media do {} é: {}" .format(nome_aluno,media))
print("A media do {0} é: {1}" .format(nome_aluno,media))
print("A media do {n} é: {m}" .format(n=nome_aluno,m=media))
#
