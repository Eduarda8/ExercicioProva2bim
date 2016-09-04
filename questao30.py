preco=float(input("Diga o preço do Pão:"))
print("Padaria - Tabela de preços :")
P= 1
while(P<=50):
	print(P," - R$ ",(P*preco))
	P += 1
