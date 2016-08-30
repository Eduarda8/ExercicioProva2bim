'''
Questão 14 :
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
Resposta :
'''
par, impar = 0, 0
for i in range(10):
    n = int(input
    (" - Entre com um número: "))
    if n%2==0: par+=1
    else: impar+=1
print ("- %d números pares, %d números impares"%(par,impar))
