#Thiago Henrique dos Santos

letra = str(input('Entre com uma letra: '))
string = input('Entre com uma frase: ')
i= 0
indices = ''
aux1 = 0
aux2 = 0
while i < len(string):
    if string[i] == letra:
        indices += str(i)+','
    i += 1

a = indices.split(',')
if len(indices) > 2:
    print (string[int(a[0])+1:int(a[-2])])
elif len(indices) == 2:
    print(string[int(a[0])])
else:
    print ('Nenhuma ocorrencia desta letra')
