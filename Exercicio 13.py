#Thiago Henrique dos Santos

import re
frase = str(input('Entre com uma String: ' ))
b = re.split('\;|\.|\,| ',frase)

print ('Quantidade de palavras digitadas: ',len(b))

