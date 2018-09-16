#Thiago Henrique dos Santos

letra = input("Entre com uma letra: ")
frase = input("Entre com uma frase: ")
cont = 0
i=0

while i<len(frase):
    if frase[i] == letra:
        cont+=1
    i+=1
print (cont)
