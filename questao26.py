'''
Questão 26 :
Numa eleição existem três candidatos. Faça um programa que peça o número
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato.
Resposta :
'''
eleitores = int(input("Digite a quantidade de eleitores:"))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(eleitores):
    voto = int(input("Digite o numero do candidato :"))
    if voto==1:
    	candidato1 = candidato1 + 1
    elif voto==2:
    	candidato2 = candidato2 + 1
    elif voto==3:
    	candidato3 = candidato3 + 1
print("O candidato 1 teve ", candidato1, " votos")
print("O candidato 2 teve ", candidato2, " votos")
print("O candidato 3 teve ", candidato3, " votos")
