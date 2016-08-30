'''
Questão 13 :
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
Resposta :
'''
b =int(input("Informe um valo:"))
expor =int(input("Informe um valor:"))
a =1
result =1
while (a <= result):
    result = result * b
    a=a +1
print("")
print("O 1º numero:",b)
print("o 2º numero:",expor)
print(b,"elevado a",expor,"que é igual a: ",result)
