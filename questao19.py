'''
Questão 19 :
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
Resposta :
'''
Num = int(input("Qantos numeros vao ser calculados :"))
Primeiro = int(input("Insira um numero que esteja entre 0 e 1000 :"))
while (Primeiro<=0 or Primeiro>1000):
    print("O valor digitado ultrapasou 1000 ou é menor que 1")
    Primeiro = int(input("Insira um numero que esteja entre 0 e 1000 :"))
Ct = 1
Maior  = Primeiro
Menor  = Primeiro
Soma  = Primeiro
while (Ct<Num):
    Aux = int(input("Insira um numero que esteja entre 0 e 1000 :"))
    while (Aux<=0 or Aux>1000):
        print("O valor digitado ultrapasou 1000 ou é menor que 1")
        Aux = int(input("Insira um numero que esteja entre 0 e 1000 :"))  
    if (Aux>Maior):
        Maior = Aux
    elif (Aux<Menor):
        Menor = Aux  
    Soma = Soma + Aux  
    Ct = Ct + 1
 
print("O maior Número é: ", Maior)
print("O menor Número é: ", Menor)
print("O valor da Soma é: ", Soma)


