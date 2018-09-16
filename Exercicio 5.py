#Thiago Henrique dos Santos

x = int(input('Qual o valor de X: '))
n = int(input('Qual o valor de N: '))

exponencial = 1
aux = 1 

while n > 0:
    exponencial = x * exponencial
    aux = aux * n
    n -= 1

print ('Resultado: ',exponencial/aux)
    
