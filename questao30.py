'''
Questão 30 :
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
contratado para desenvolver o programa que monta a tabela de preços de pães,
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o
exemplo abaixo :
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
'''
Pão=int(input("Diga quantos Pão você deseja levar :"))
print("O Preço do pão é:",Pão)
print("Padaria - Tabela de preços :")
P= 1
while(P<50):
	print(P,"Reais:",(P*1.99))
	P += 1
	print(P,"-R$%.2f"%(P*Pão))
