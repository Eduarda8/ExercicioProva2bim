'''
Questão 23 :
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número
de divisões que ele executou para encontrar os números primos. Serão avaliados
o funcionamento, o estilo e o número de testes (divisões) executados.
Resposta :
'''
        
Num = int(input("Digite um numero :"))
cont = 0
div = []
for i in range( Num ):
    if Num%(i+1) == 0:
        cont += 1  
        div.append(i+1)
if cont == 2:
    print ("O numero é primo, porque é divisivel por :",div)
else:
    print ("O numero não é primo, porque é divisivel por :",div)
