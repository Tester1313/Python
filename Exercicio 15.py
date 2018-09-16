#Thiago Henrique dos Santos

frase = str(input('Entre com uma palavra: ' ))
stringMinuscula = frase.lower()

## Função que inverte a palavra
stringInvertida = stringMinuscula[::-1]

if stringInvertida == stringMinuscula:
    print("Esta palavra é palindroma")
else:
    print("Esta palavra não é palindroma")

