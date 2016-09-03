'''
Questão 27 :
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos
para cada turma. As turmas não podem ter mais de 40 alunos.
Resposta :
'''


NumT = int(input ("Digite a quantidade de Turmas :"))
soma = 0 
for e in range( 1, NumT+ 1 ):
	Qunt_A = int(input("Digite a quantidade de alunos de cada turma :"))
	while( Qunt_A > 40 ):	
		print ("A quantidade de turmas não pode ser maior que 40!!")
		print("Entrada Inválida")
		Qunt_A = int(input("Digite a quantidade de alunos de cada turma :"))
	soma = soma + Qunt_A
	e=e +1
media = soma/NumT
print("A média de alunos é: ",media)

