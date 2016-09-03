'''
Questão 25 :
Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60
e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme
a média calculada.
Resposta :
'''
Num = int(input("Digite um número : "))
Soma = 0 
cont = 0  
for x in range(Num):
	a = int(input("Digite uma idade na sequência : "))
	Soma = Soma + a
	cont = cont + 1
media = Soma/cont
if media>=0 and media<=25:
  print("Jovem")
elif media>=26 and media<=60:
  print("Adulta")
elif media>60:
  print("Idosa")
