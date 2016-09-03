'''
Questão 20 :
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
Resposta :
'''
quantidade = int(input("Digite quantos fatoriais voce quer calcular:"))

for i in range(quantidade):
	numero = int(input("Insira um numero:"))

	while (numero > 16 or numero < 0): 
		print ("Numeros entre que 16 e 0 por favor")
		numero = int(input("Insira um numero:"))

	NC = numero  
	FT = 1

	while (NC > 0 ):
		FT = FT * NC
		NC -= 1
		
	print("O Valaor Fatorial de",numero,"=",FT)
	
