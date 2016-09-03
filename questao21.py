'''
Questão 21 :
Faça um programa que peça um número inteiro e determine se ele é ou
não um número primo. Um número primo é aquele que é divisível somente
por ele mesmo e por 1.
Resposta :
'''
# Usando com o while :
Num = int(input("Digite um numero :"))
cont = 0
i = 1
while i<=Num:
    if Num%i==0:
        cont = cont+1
    i = i+1
if cont>2:
    print("Nao e primo")
else:
    print("E primo")

# Usando o for :
Num = int(input("Digite um numero :"))
cont = 0
for i in range(1,Num+1):
    if Num%i==0:
        cont = cont+1
if cont>2:
    print("Nao e primo")
else:
    print("E primo")

