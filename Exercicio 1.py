#Thiago Henrique dos Santos

num1=int(input('Digite um número: '))
i = num1
a = 0

while i > 0 and num1 != 1:
    if num1%i == 0:
        a += 1
      
    i -= 1

if a>2 or num1==1:
    print ('Não é um número primo');
else:
    print ('Número primo.');
