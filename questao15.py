
'''
Questão 15 :
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
n = int(input("Informe um valor :"))
sq = 1
e= 0
t= 1
print("e")
while (sq<n):
    j= e + t
    print(j)
    e = t
    t = j
    sq = sq +1
