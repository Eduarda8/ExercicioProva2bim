#Altere o programa anterior para mostrar no final a soma dos números.
inicio=eval(input("Digite o valor inicial do intervalo :"))
fim=eval(input("Digite o valor final do intervalo :"))

if (inicio <= fim):
    auxiliar = inicio +1
    soma = 0
    while (auxiliar < fim):
	print (auxiliar)
        soma = auxiliar + soma
        auxiliar +=1

else:
	
	print("Entrada Invalida")
print("O valor inicial era :", inicio)
print("O valor final era :", fim)
print("A soma dos intervalos é :", soma)
