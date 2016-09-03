'''
Questão 24 :
Faça um programa que calcule o mostre a média aritmética de N notas.
Resposta :
'''
quantidade = int(input("Digite a quantidade de notas"))
soma = 0

for i in range(quantidade):
    soma += int(input("Digite uma nota:"))
print("A media e: ", soma/quantidade)
