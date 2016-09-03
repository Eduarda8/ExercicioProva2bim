'''
Questão 24 :
Faça um programa que calcule o mostre a média aritmética de N notas.
Resposta :
'''
Num = int(input("Digite um numero : "))
Soma = 0 
cont = 0  
for x in range(Num):
	a = int(input("Digite um numero na sequência : "))
	if a > 0: 
		Soma = Soma + a
	cont = cont + 1

print ("O resultado é : ", Soma)
