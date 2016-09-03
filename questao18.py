'''
Questão 18 :
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
Resposta :
'''
N = int(input("Quantos números seram calculados:"))
Aux = 1 
Num = int(input("Insira um número:"))
Maior = Num 
Menor = Num 
Soma = 0 
while (Aux<=N):
    if (Aux<N):
        Num = int(input("Digite um número:"))
    if (Num>Maior):
        Maior = Num
    elif (Num<Menor):
        Menor = Num
    Soma = Soma + Num
    Aux = Aux + 1

print("O Numero maior é: ", Maior)
print("O Numero menor é: ", Menor)
print("O valor da Soma é: ", Soma)

