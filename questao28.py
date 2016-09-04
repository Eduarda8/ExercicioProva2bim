'''
Questão 28 :
Faça um programa que calcule o valor total investido por um colecionador em
sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá
informar a quantidade de CDs e o valor para em cada um.
Resposta :
'''

quantidade = int(input("Digite a quantidade de CDs:"))
soma =0
for i in range(quantidade):
    num = int(input("Digite o valor do cd:"))
    soma = soma + num
print("Gastou no total: ", soma)
print("Gastou em media: ", soma/quantidade)

