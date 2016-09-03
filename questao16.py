'''
Questão 16 :
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
Resposta :
'''

print("Programa da série de Fibonacci gerando ate mais do valor de 500:\n") 

s_q = 1
a = 0 
e = 1
t = 0 
print("e")
while ( t  < 500):
    t = a + e 
    print(t)
    a = e 
    e = t 
    s_q  +=1
