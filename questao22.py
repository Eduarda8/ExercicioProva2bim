'''
Questao 22 :
Altere o programa de cálculo dos números primos, informando, caso o número
não seja primo, por quais número ele é divisível.
Resposta :
'''
Num = int(input("Digite um numero :"))
cont = 0
for i in range(1,Num+1):
    if Num%i==0:
        cont +=1
        print("O numero é divisel por ", i)
if cont == 2 :
    print("O numero é primo!")
else:
    print("O numero não é primo")
