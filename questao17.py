'''
 Questão 17 :
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
Resposta :
'''
numero = int(input("Insira um numero:"))
NC = numero  
FT = 1
while (NC > 0 ):
    FT = FT * NC
    NC -= 1
    
print("O Valor Fatorial de",numero,"=",FT)


